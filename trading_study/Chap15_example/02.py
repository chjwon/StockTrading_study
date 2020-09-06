# y=x^2 (x>=0)의 그래프
# 'ro'스타일의 그래프

import matplotlib.pyplot as plt

# x,y값 동시에 받기
# y=x^2 그래프
# 코드
x = range(0,100)
y = [v*v for v in x]
plt.plot(x,y,'ro')
plt.show()

# y값 구현시  for문으로 append시켜도 가능하지만 가독성이 좋지 않음
# y=[]
# for v in x:
#     y.append(v*v)


# plot() 안에 'ro'(red+o는 모양)는 각 점을 빨간색 원으로 바꿔준다.
# 작성하지 않으면 구간사이를 파란색으로 직선으로 연결하는 스타일이다.('b-')
# 색상 종류
# b/blue, g/green, r/red, c/cyan, m/magenta, y/yellow, k/black, w/white
# 마커 종류
# o/circle, v/triangle_down(역삼각형), ^/triangle_up(삼각형), s/square, +/plus, ./point