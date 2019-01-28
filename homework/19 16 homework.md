# 2019-01-23

# 16.homework

### 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

### 해당 테이블에 다음과 같이 데이터를 입력한다.

```
sqlite> CREATE TABLE friends(
   ...> id INTEGER,
   ...> name TEXT,
   ...> location TEXT
   ...> );

sqlite> INSERT INTO friends(id,name,location)
   ...> VALUES(1,'justin','Seoul')
sqlite> INSERT INTO friends(id,name,location)
   ...> VALUES(2,'Simon','New York');
sqlite> INSERT INTO friends(id,name,location)
   ...> VALUES(3,'Chang','Las Vegas');
sqlite> INSERT INTO friends(id,name,location)
   ...> VALUES(4,'John','Sydney');                    
sqlite> select * from friends;

id          name        location  
----------  ----------  ----------
1           justin      Seoul     
2           Simon       New York  
3           Chang       Las Vegas 
4           John        Sydney    
```



### 스키마를 다음과 같이 변경한다.

### 데이터를 다음과 같이 추가한다.

```
sqlite> alter table friends add column 'married' INTEGER


sqlite> INSERT INTO friends(id,name,location,married)
   ...> VALUES(1,'Justin','LA',1);
sqlite> INSERT INTO friends(id,name,location,married)
   ...> VALUES(2,'Simon','New York',0);
sqlite> INSERT INTO friends(id,name,location,married)
   ...> VALUES(3,'Chang','LasVegas',0);                 
sqlite> INSERT INTO friends(id,name,location,married)
   ...> VALUES(4,'John','Sydney',0);
sqlite> select * from friends;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
2           Simon       New York    0         
3           Chang       LasVegas    0         
4           John        Sydney      0  
```



### 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.

### married 가 0 인 데이터를 모두 삭제한다.

```
sqlite> DELETE FROM friends WHERE id=2;
sqlite> DELETE FROM friends WHERE id=3;
sqlite> select * from friends;
id          name        location    married   
----------  ----------  ----------  ----------
1           Justin      LA          1         
4           John        Sydney      0    
```

