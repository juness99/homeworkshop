# 08workshop

### 1. Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’ 페이지를 만들어보세요.



#### A.PY

```python
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dictionary/<string:word>")
def dictionary(word):
    
    i={"apple":"사과","simple":"쉬운","money":"돈"}
    if word in dict.keys(i):
        a=f"{word}은(는){i[word]}!!"
    else:
        a=f"{word}은(는) 나만의 단어장에 없는 단어입니다!"
        
    return render_template("dictionary.html",a=a)
    
    

if __name__ == "__main__":
    #이렇게 실행 명령어를 변경할 수 있다. debug의장점 재실행을 안해도 됨!!
    app.run(debug=True,host="0.0.0.0",port=8080) #앱을 실행해줘
```



### dictionary.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{a}}</h1>
</body>
</html>
```



