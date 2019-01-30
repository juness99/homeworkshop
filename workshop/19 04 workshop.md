# workshop 04



## 1.



```
n = int(input("숫자를 입력하세요 : "))
m = int(input("숫자를 입력하세요 : "))
a = ('*'*n)+"\n"
print(a*m)
```



![1546850050170](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1546850050170.png)



## 2.



```
student = {'python':80, 'algorithm':99, 'django':89, 'flask':83}
a=0
for score in student.values():
    a=score+a
print(a/len(student))
```

87.75



## 3.

    blood = ['A','B','O','A','AB','AB','O','A','B','O','B','AB']
    A = 0
    B = 0
    O = 0
    AB = 0
    for i in blood:
        if i =='A':
            A=A+1
        elif i == 'B':
            B=B+1
        elif i=='O':
    		O=O+1
    	elif i=='AB':
        	AB=AB+1
    else:
        print(f"A형:{A},B형:{B},O형:{O},AB형:{AB}")
```
A형:3,B형:3,O형:3,AB형:3
```