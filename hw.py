import numpy as np
import matplotlib.pyplot as plt

l1 = np.arange(-5,5,0.1)
print(l1)
eq1 = l1
eq2 = l1**2
eq3 = l1**3

plt.plot(eq1,'r--',eq1,eq2,'g--',eq1,eq3,'b--')
plt.show()

#--

m  = int(input("Please enter Val for M "))
c = int(input("please enter val for c "))
x = np.arange(-20,20,1)


eq_1 = m*x + c

plt.plot(eq_1)
plt.show()