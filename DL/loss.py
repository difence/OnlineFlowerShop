import matplotlib.pyplot as plt

name = 'CNN'

f = open('trainLoss-{}.txt'.format(name), 'r')

a = f.readlines()
f.close()
x0 = a[0].split(" ")
y0 = a[1].split(" ")
z0 = a[2].split(" ")
# t0 = a[3].split(" ")
x = []
y = []
z = []
t = []

for i in range(len(x0)):
    x.append(float(x0[i]))
    y.append(float(y0[i]))
    z.append(float(z0[i]))
    # t.append(float(t0[i]))

plt.plot(range(1, len(x) + 1), x, label='loss', color='lightblue')
# plt.plot(range(1, len(t) + 1), t, label='val_loss', color='pink')
plt.legend()
plt.title('The Loss Score Of {}'.format(name))
plt.xlabel("epoch size")
plt.ylabel("rate")
plt.show()

plt.plot(range(1, len(y) + 1), y, label='accuracy', color='pink')
plt.plot(range(1, len(z) + 1), z, label='val_accuracy', color='lightblue')
plt.legend()
plt.title('The Accuracy Score Of {}'.format(name))
plt.xlabel("epoch size")
plt.ylabel("rate")
plt.show()
