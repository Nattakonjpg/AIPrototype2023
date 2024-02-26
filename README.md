# AIPrototype2023
 Nattakon Puangkaew 
 ID : 633021015-9 : SIDS

## Al Prototype Class 1
- [Facebook](https://www.facebook.com/groups/356929536868115)

### เรียน 8 บท
Command line → บท 1 - บท 4

### Homework

1. Create Account Cloud
2. Google Drive : Paste URL github
3. ubuntu 

## AI Prototype Class 2

### Create Virtual Machine

1. Portal azure
    1. Virtual Machine
    2. Resource group = Folder Collect Service
    3. in terminal
    
    ```jsx
    ssh nattakonpu@ip #connect cloud
    password Nattakonpu12
    exit #getout VM 
    htop = check process
    sudo chmod 755 username #set group user and other
    7=host read write excute, 5 = group read excute, 5 = other read excute 
    ```
    
2. Scp File
    
    ```jsx
    scp -r testfolder1/ nattakonpu@4.216.171.68 # folder -> pc to cloud
    scp nattakonpu@IP:/home/nattakonpu/file.. ~/. #file -> Cloud to pc
    ```
    
    ### Azure Cloud Shell
    
    Shell is on internet it make our connect easy
    
    1. Upload file → it install in my pc 
    2. Scp file to Cloud VM
    
    ### File type
    
    1. r = 4 read
    
   2.  w = 2 write
    
   3. x = 1 execute ( run )
    
## AI Prototype Class 3

```python
sudo = install for everyone 
**if want install something for only one should create enviorment**

**Create enviorment**
conda create -n myenv python=3.9 #-n (name)= new enviorment name
conda activate mypy38 # use this ev
conda deactiveate # exit ev
```

```python
**Create Jupyter notebook**
conda install notebook #install
jupyter notebook #Use notebook
```

### Notebook on Cloud

- ต้องการใช้ web ในเครื่องที่อยู่บน Cloud  ใช้คำสั่ง screen ถ้าปิด หรือ เน็ตหลุด  section จะหาย 

```python
screen -S (name) #start Screen
screen -S sc1
cltr+A D # ตัดตัวเองออกจาก Screen = detech from screen
screen -R (name) #Retech 
screen -R sc1 
screen -ls # check how many screen right now
cltr+A k y = delte screen
```

### Screen Notebook

```python
#create notebook
scree -s notebook
jupyter notebook
ssh -L 8866:localhost:8888 nattakonpu@ip
(สร้าง link port 8866 map to 8888 เครื่อง nattakonpu@ip)
```

http://localhost:8888/tree?token=a8539a989021ea1e6909bb805a9bc4777054eeec8711d9b3

### Github on linux

```python
git config --global user.name "nattakonjpg"
git config --global user.email "nattakonpu@kkumail.com"
git clone https://github.com/Nattakonjpg/AIPrototype2023.git
Vi Readme.md# Can config readme file
Ctrl wq = exit = quite write
Ctrl q! = exit = quite no write
git status # ดูว่าไฟล์ไหนแก้ไขไปบ้าง
git add # upfile to github
git commit -m*add myname* # บอกว่าแก้อะไร
```
## AI Prototype Class 4
Step this week

1. in folder ubuntu → folder AIPrototype66
2. code [testpy.py](http://testpy.py) # สร้าง folder 
3. Ctrl + S #ได้ไฟล์ py ที่เราเขียน

```python
#Step after create file.py
git pull # ก่อนตลอดก่อนเริ่มแก้โค๊ด เรียกให้อัพเดท code
git status # Check 
git add (filename)
git commit -m "..."
git push
	nattakonjpg
	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
#upload file to github on internet
```

1. **In vm : folder code → AI** 

```python
git pull # เรียกเวอร์ชั่นล่าสุด
python (filename)
```

### argparse : รับ input ข้างนอก

```python
import argparse 

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--num',
        type=int,
        required=True,
        help='input for the multiplyby9 function'
    )
    parser.add_argument(
        '--XX',
        type=int,
        default=7,
        help='input for the multiplyby9 function'
    )
    args = parser.parse_args()
    return args

def printhello(): 
    print("hell word") 

def multiplyby9(input_V):
    print(9*input_V)

if __name__=="__main__": #flow program

    input_V = parse_input()
    print(f'the input xx is {input_V.XX}') #รับค่า
    print("we are in the main function")
    multiplyby9(input_V.num)
    printhello()
```

1. Import package : argparse : รับ input ข้างนอก
2. Create function **parse_input (** ให้รับตัวแปรตอนเรารัน python)
    
    1. num = จำเป็นต้องใส่ ิเป็นตัวเลข
    
    2. xx = ไม่จำเป็นต้องใส่ ถ้าใส่จะเป็นเลข ถ้าไม่ใส่จะเป็น “7”
    
3. function hello word
4. function การคูณ
    1. 9*(input) (xx=ตัวเลขที่ใส่ไม่ใส่ =7)
5. main function (flow follow after this)
    - เริ่มจาก รับค่าตัวแปร input_V = parse_input() {function}
    - print(the input xx i (ค่าตัวแปร x ไม่มีก็=7)
    - print("we are in the main function")
    - function การคูณ 9*ตัวแปร x 
    - print(”hello”) function
## AI Prototype Class 5
- นำเสนอการบ้าน Subprocess 
## AI Prototype Class 6
- Goal this class = writing web from python
- **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**
    1. Web page
        1. Show information about project 
    2. Web App
        1. User can use our model form this web
- **Web 3 type**
    - **Webpage = no function , only for looking information**
        - html, css, java script
            - css = can dowload from other
    - **Web app = add  Server Side Script**
        - Using Package Flask → Python
    - **Web Service = Server Side Script only**
        - for only User use
### [Github](https://github.com/Nattakonjpg/Valolyze/blob/main/index.html)

## AI Prototype Class 7
```python
from flask import Flask, request, render_template, make_response

import json

app = Flask(_-name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

if __name__== "__main__"
    app.run(host='0.0.0.0',debug=True,port=50001)#host='0.0.0.0", port=500
```

- from flask : import libary
- app = Flask(__name__)
- def helloworld():
- route(”/”) = ในเว็บ ถ้าเปิดแบบนี้ www.flask.com/
    - จะรัน function hello word
    200 = run success
    404 = can’t find icon website
    202.28.118.110 = ip เครื่อง
    **port:50001 :** port 5001 ให้สามารถเข้าได้ setting ใน vm
    
## AI Prototype Class 8
**conda activate mypy38**

post : ส่งทุกอย่างใน url

get : ส่ง

### Web Service

-  Program ลอยๆ ส่ง input รับ input มาใช้งานต่อ

### Web Site

- มี input ให้อ่านเฉยๆ

### web app 

- มี input แล้วได้ output ให้ใช้

## Homework

1. webpage มากกว่าเดิม
2. web project
    1. upload vdo ก็เป็นอย่างงั้น

## Flask Structure

![Flask](Image/Flask%20stru.png)

- **fw**
    - → อันนี้คือชื่อของ Virtual Environment โดยในโฟลเดอร์นี้จะเอาไว้ใช้เก็บไลบรารี่ต่าง ๆ ที่เราได้ทำการติดตั้งผ่าน pip นั่นเอง
- **templates  (folder ต้องมี “s” เท่านั้น)**
    - → เป็นโฟลเดอร์ที่เอาไว้ใช้เก็บไฟล์ HTML
- **app.py**
    - → เป็นไฟล์หลักที่เอาไว้ใช้เขียนและเอาไว้รัน flask นั่นเอง แน่นอนว่าเราจะเขียนโค้ดในไฟล์ที่บ่อยที่สุด
- **static**
    - → เป็นโฟลเดอร์ที่จะเอาไว้ใช้เก็บไฟล์ static(ไฟล์ที่ไม่มีการเปลี่ยนแปลงของคอนเทนต์) ต่าง ๆ เช่น JavaScript(js), CSS และไฟล์รูปภาพนามสกุลต่าง ๆ เช่น jpg, png เป็นต้น ซึ่งเราจะต้องเก็บไฟล์เหล่านี้ ไว้ที่โฟลเดอร์ static

## AI Prototype Class 9+10
### Deep Learning

- input = image ( This class)

## **Theory**

### 1. Classical

→ แปลงให้อยู่ในรูป Vector → ชุดของตัวเลข {x1,x2,x3,…,xn} → data is feature vector have n dimension

### 2. Deep Learning

→ Feature engineering

→ Histogram of Oriented Gradients

→ Image 

→ Sobel filter

→ Gx, Gy = ค่ามาก = แนวตั้ง , ค่าน้อย = ไม่ตั้ง

---

![1](Image/1.png)
x = feateur

w =weight

---

![2](Image/2.png)
![3](Image/3.png)
![4](Image/4.png)
ผลรวมของ sum > 0 จะผ่าน activation function → output = 1 แต่ค่าจริงๆ = 0

ผลรวมของ sum < 0 จะผ่าน avtivation function → output = 0

---

### Fully connected / Dense layer

Input Node ขึ้นอยู่กับ feature = n

Input Node → layer 1 → layer 2 → output

![5](Image/5.png)

---

### Deep Learning

![6](Image/6.png)

: max pooling = สรุปเฉพาะจุดเด่น

activation function = กำหนดค่าที่ไปคูณให้อยู่ใน range ต้องการ

---

### Soble filter

![7](Image/7.png)

---

### Binary cross entropy loss

![8](Image/8.png)
→ for Many Class
## AI Prototype Class 11 code deep learning
[Keras: API ระดับสูงสำหรับ TensorFlow  |  TensorFlow Core](https://www.tensorflow.org/guide/keras?hl=th)

[Google Colaboratory](https://colab.research.google.com/drive/1sQ7SugSz_5I0j0JrhzXmqufq3NwAQWv7)
### Network Deeplearning

1. Sequential (ง่ายๆ สร้างได้แบบไม่ซับซ้อน (วิ่งเป็นเส้นตรง)
2. Functional ( ยากขึ้น ปรับเส้นทางให้มีความซับซ้อนได้)

Deep Learning inception 

![9](Image/9.png)

![10](Image/10.png)

### Sequential network

![11](Image/11.png)

- นำภาพผ่าน Conv2D size 32layer มี 3 channel 3*3 ผ่าน filter 3*3
- max pooling ดูทุกๆ 2pixel ทั้งแนวตั้ง แนวนอน สรุปเหลือ 1
- นำภาพผ่าน Conv2D size 64 layer

![12](Image/12.png)

- Flatten เอาพารามิเตอร์มายืดเป็นเส้นตรง
- ผ่าน Dense = fully connected
- output = 10 class
### Functional network
#### Data pipline

- data ในแต่ละรอบให้โหลดมาทีละส่วนๆ
    - Folder in google drive
1. Image ornamentation
![13](Image/13.png)
