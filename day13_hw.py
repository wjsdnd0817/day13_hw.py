# day13_hw.py

# 움직이는 거북이 8마리 피하기


import turtle as t 
import random # 랜덤모듈 사용



t.speed(0) # 검은색 거북이의 속도


t.up() # 선을 그리지 않고 이동하기 위해
t.goto(-300,-200) # 테두리 벽의 시작점으로 이동
t.pendown() # 선그리기 시작
t.seth(90) # 거북이의 방향을 위로 설정
for x in range(4): # 테두리벽 그리기
    t.fd(500)
    t.rt(90)

t.up() # 선을 그리지 않고 이동하기 위해
t.goto(random.randint(-300,200),random.randint(-200,300)) # 거북이의 시작위치 랜덤설정
t.seth(random.randint(0,360)) # 거북이의 시작방향 랜덤설정
t.down() # 선 그리기 시작

# 움직이는 장애물(거북이) 8마리 세팅
t_1=t.Turtle()
t_2=t.Turtle()
t_3=t.Turtle()
t_4=t.Turtle()
t_5=t.Turtle()
t_6=t.Turtle()
t_7=t.Turtle()
t_8=t.Turtle()

# 모든 장애물의 색을 빨강으로 지정
t_1.color("Red")
t_2.color("Red")
t_3.color("Red")
t_4.color("Red")
t_5.color("Red")
t_6.color("Red")
t_7.color("Red")
t_8.color("Red")
    
# 장애물들이 선을 그리지 않고 이동하기
# 모두 선을 그리면 지저분하기 때문에
t_1.up()
t_2.up()
t_3.up()
t_4.up()
t_5.up()
t_6.up()
t_7.up()
t_8.up()

# 장애물들이 층별로 랜덤의 x좌표 설정
# 장애물들이 층별로 가로로 왔다갔다 하기위해
t_1.goto(random.randint(-300,200),-150)
t_1.seth(0)
t_2.goto(random.randint(-300,200),-100)
t_2.seth(0)
t_3.goto(random.randint(-300,200),-50)
t_3.seth(0)
t_4.goto(random.randint(-300,200),-0)
t_4.seth(0)
t_5.goto(random.randint(-300,200),50)
t_5.seth(0)
t_6.goto(random.randint(-300,200),100)
t_6.seth(0)
t_7.goto(random.randint(-300,200),150)
t_7.seth(0)
t_8.goto(random.randint(-300,200),220)
t_8.seth(0)

    


# 프로그램 시작
while True:
    a= t.xcor() # a는 검은거북이의 x좌표
    b= t.ycor() # b는 검은거북이의 y좌표
    c= t.heading() # c는 검은거북이가 보는방향 설정
# 빨간 거북이(장애물)의 x좌표 설정
    d_1=t_1.xcor() 
    d_2=t_2.xcor()
    d_3=t_3.xcor()
    d_4=t_4.xcor()
    d_5=t_5.xcor()
    d_6=t_6.xcor()
    d_7=t_7.xcor()
    d_8=t_8.xcor()

    if a <= -300: # 검은 거북이가 왼쪽 테두리에 부딪힌다면
        t.seth(360-(c-180)) # 반사각으로 방향을 돌린다
        t.fd(1) # 방향을 돌린후 전진
    if a >= 200: # 검은 거북이가 오른쪽 테두리에 부딪힌다면
        t.seth(360-(c-180)) # 반사각으로 방향을 돌린다
        t.fd(1) # 방향을 돌린후 전진
    if b <= -200: # 검은 거북이가 아래쪽 테두리에 부딪힌다면
        t.seth(360-c) # 반사각으로 방향을 돌린다
        t.fd(1) # 방향을 돌린후 전진
    if b >= 300: # 검은거북이가 위쪽 테두리에 부딪힌다면 
        t.seth(360-c) #  반사각으로 방향을 돌린다
        t.fd(1) # 방향을 돌린후 전진
# 검은거북이가 빨간거북이를 만나면 방향을 돌린후 전진
    if a==d_1:
        t.seth(360-c)
        t.fd(1)
    if a==d_2 :
        t.seth(360-c)
        t.fd(1)
    if a==d_3:
        t.seth(360-c)
        t.fd(1)
    if a==d_4:
        t.seth(360-c)
        t.fd(1)
    if a==d_5:
        t.seth(360-c)
        t.fd(1)
    if a==d_6:
        t.seth(360-c)
        t.fd(1)
    if a==d_7:
        t.seth(360-c)
        t.fd(1)
# 빨간거북이들이 좌우의 테두리에 부딪힌다면 방향을 돌린다
# if 조건은 모두 좌우의 테두리에 부딪히는것
    if d_1<=-300 or d_1>=200:
        t_1.rt(180)
        t_1.fd(1)
    if d_2<=-300 or d_2>=200:
        t_2.rt(180)
        t_2.fd(2)
    if d_3<=-300 or d_3>=200:
        t_3.rt(180)
        t_3.fd(1)
    if d_4<=-300 or d_4>=200:
        t_4.rt(180)
        t_4.fd(1)
    if d_5<=-300 or d_5>=200:
        t_5.rt(180)
        t_5.fd(1)
    if d_6<=-300 or d_6>=200:
        t_6.rt(180)
        t_6.fd(1)
    if d_7<=-300 or d_7>=200:
        t_7.rt(180)
        t_7.fd(1)
    if d_8<=-300 or d_8>=200:
        t_8.rt(180)
        t_8.fd(1)
# 아무거도 부딪히지 않는다면 앞으로 전진한다
    else:
        t.fd(1)
        t_1.fd(1)
        t_2.fd(1)
        t_3.fd(1)
        t_4.fd(1)
        t_5.fd(1)
        t_6.fd(1)
        t_7.fd(1)
        t_8.fd(1)
    


