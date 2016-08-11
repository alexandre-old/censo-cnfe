# censo-cnfe

```
(censo-cnfe) alexandre ~/Development/python/censo-cnfe (master) 
 ~>time ./manage.py export-to-json examples/35188000500.zip /tmp/censo-cnfe/

 Parsing file: '35188000500'
Created file: '35188000500'.json

 Ok, Done!


real	2m4.164s
user	2m1.580s
sys	0m4.300s
```

```
alexandre /tmp 
 ~>unzip 35188000500.zip 
Archive:  35188000500.zip
  inflating: 35188000500.TXT         
alexandre /tmp 
 ~>wc -l 35188000500.TXT 
301638 35188000500.TXT
```
