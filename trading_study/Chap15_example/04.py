# 한 화면에 여러개의 그래프 그리기
import matplotlib.pyplot as plt

# 코드
fig = plt.figure()
# (2,1,1)의 의미 2x1의 subplot을 생성한다는 의미이고 1번째 subplot을 뜻한다.
ax1 = fig.add_subplot(2,1,1)
# (2,1,2)의 의미 2x1의 subplot을 생성한다는 의미이고 2번째 subplot을 뜻한다.
ax2 = fig.add_subplot(2,1,2)

x=range(0,100)
y = [v*v for v in x]

ax1.plot(x,y)
ax2.plot(x,y)

plt.show()
