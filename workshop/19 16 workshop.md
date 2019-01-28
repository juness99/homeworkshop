# 2019-01-23

# 16.workshop

### 저번 워크샵에서 아래 표와 같은 DB를 제작한 상태다.

###  해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라.

```
sqlite> alter table bands add column 'members' INTEGER;         
sqlite> select * from bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        NULL      
2           Coldplay    1998        NULL      
3           MCR         2001        NULL     
```

### 데이터삽입

```
sqlite> UPDATE bands SET members=4 WHERE id=1;
sqlite> select * from bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        NULL      
3           MCR         2001        NULL      
sqlite> UPDATE bands SET members=5 WHERE id=2;                  
sqlite> UPDATE bands SET members=9 WHERE id=3;                 
sqlite> select * from bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        9    
```



###  Id 가 3인 레코드의 members 를 5로 수정하라.

```
sqlite> UPDATE bands SET members=5 WHERE id=3;                  
sqlite> select * from bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
2           Coldplay    1998        5         
3           MCR         2001        5  
```



###  Id 가 2인 레코드를 삭제하라

```
sqlite> DELETE FROM bands WHERE id=2;
sqlite> select * from bands;
id          name        debut       members   
----------  ----------  ----------  ----------
1           Queen       1973        4         
3           MCR         2001        5         
```

