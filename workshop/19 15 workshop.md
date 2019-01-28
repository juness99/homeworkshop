# 2019-01-22

# workshop

### 1.아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅 시다.



```
sqlite> CREATE TABLE bands(
   ...> id INTEGER,
   ...> name TEXT,
   ...> debut INTEGER
   ...> );
sqlite> .table
bands
sqlite> .schema bands
CREATE TABLE bands(
id INTEGER,
name TEXT,
debut INTEGER
);
sqlite> INSERT INTO bands(id,name,debut)
   ...> VALUES(1,'Queen',1973)
   ...> ;
sqlite> .headers on
sqlite> .mode column  
sqlite> INSERT INTO bands(id,name,debut)
   ...> VALUES(2,'Coldplay',1998);
sqlite> INSERT INTO bands(id,name,debut)
   ...> VALUES(3,'MCR',2001);
sqlite> select * from bands;

id          name        debut     
----------  ----------  ----------
1           Queen       1973      
2           Coldplay    1998      
3           MCR         2001 
```



### 2.bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```
sqlite> SELECT id,name FROM bands;

id          name      
----------  ----------
1           Queen     
2           Coldplay  
3           MCR   
```



### 3.bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.



```
sqlite> SELECT name FROM bands
   ...> WHERE debut<2000;
name      
----------
Queen     
Coldplay  
```

