#(0,0) AxesSubplot에 그래프를 출력
import matplotlib.pyplot as plt

fig = plt.figure()

# type(fig)

ax = fig.add_subplot(1,1,1)

# type(ax)

fig, ax_list = plt.subplots(2, 2)
ax_list[0][0].plot([1, 2, 3, 4])
plt.show()