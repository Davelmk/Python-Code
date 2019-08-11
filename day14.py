import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x=np.random.randn(30)
plt.plot(x,'r--o')

np.random.seed(42)
x=np.random.randn(30)
y=np.random.randn(30)

plt.title('Example')
plt.xlabel('X')
plt.ylabel('Y')

a=np.random.randn(30)
b=np.random.randn(30)
c=np.random.randn(30)
d=np.random.randn(30)

fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

A,=ax1.plot(a,'r--o')
ax1.legend([A],["A"])
B,=ax1.plot(b,'b-*')
ax2.legend([B],["B"])
C,=ax3.plot(c,'g-.+')
ax3.legend([C],["C"])
D,=ax4.plot(d,'m:x')
ax4.legend([D],["D"])