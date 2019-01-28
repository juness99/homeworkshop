# workshop 10

##### Selector 를 활용한 DOM 탐색 실습. 

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <style>
        #ssafy> p:nth-of-type(3){
            color: red;
        }
    </style>
    <div id="ssafy">
        <h2>어떤게 선택될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>   
</body>
</html>
```

답

```
nth-child는 부모기준으로 n번째를 가리키고
nth-of-type은 같은 유형의 n번째를 가리킨다.
```



