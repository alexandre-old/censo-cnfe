import collections
import functools

import couchdb
import pymongo


class CouchDB:

    def __init__(self, settings, **kwargs):
        self._settings = settings

    @property
    def server(self):
        return couchdb.Server(self._settings['server-url'])

    @property
    def db(self):
        try:
            return self.server[self._settings['db']]
        except couchdb.http.ResourceNotFound:
            return self.server.create(self._settings['db'])


class MongoDB:

    def __init__(self, settings, **kwargs):

        self._settings = settings
        self._collection = kwargs.get('collection')

    @property
    def client(self):
        return pymongo.MongoClient(
            self._settings['host'], self._settings['port']
        )

    @property
    def db(self):
        return self.client[self._settings['db']]

    @property
    def collection(self):
        return self.db[self._collection or self._settings['collection']]


@functools.singledispatch
def save(client, data):
    pass


@save.register(CouchDB)
def save_couchdb(client, data):

    if isinstance(data, dict):
        return client.db.save(data)

    elif isinstance(data, collections.Iterable):
        return [client.db.save(item) for item in data]

    else:
        raise ValueError(
            'The client does not know how to save the data {!r}'.format(data)
        )


@save.register(MongoDB)
def save_mongodb(client, data):

    if isinstance(data, dict):
        return client.collection.insert_one(data)

    elif isinstance(data, collections.Iterable):  # e.g. tuples and generators
        return client.collection.insert_many(data)

    else:
        raise ValueError(
            'The client does not know how to save the data {!r}'.format(data)
        )
