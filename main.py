import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)
plt.show()

plt.plot(x,y,'ro')
plt.show()

plt.plot(x,y,'g^')  #yrangle
plt.show()

plt.plot(x,y,'r--')
plt.show()

plt.plot(x,y,'b--')
plt.show()

plt.plot(x,y,'b-')
plt.show()

plt.plot(x,y)
plt.axis([0,10,0,20])
plt.show()


plt.plot(x,y,'r--',label = "Y = X", linewidth = 4)
plt.axis([0,10,0,50])

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Sample Graph")

plt.legend()
plt.show()

"""

x = np.arange(0,10,0.2)
print(x)
y1 = x**2
y2 = x**3

plt.plot(x,y1,'g--',x,y2,'b--')
plt.show()


# linear

m = 2
c= 3

x = np.linspace(-5,5,100)

y = m*x + c

plt.plot(x,y,'g--',label = f'y = {m}x+{c}')
plt.title("Linear Equation Graphed")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")



plt.legend()
plt.show()

##

#x = pos,  y = height

x = [1,3,5,7]
y= [2,4,1,7]

plt.bar(x,y,color = 'b')
plt.show()

plt.bar([1,3,5,7],[2,4,6,8],color = 'g')
plt.bar([2,4,6,8],[3,5,7,9],color = "r")
plt.show()

plt.bar(["Male literacy","Female Literacy"],[90,95])
plt.show()


plt.bar(["1st class","2nd class","3rd Class"],[20,40,80])
plt.show()

#custom graph

x= []
y=[]

for i in range(5):
    n=int(input("Enter X value : "))
    x.append(n)

print(x)

for j in range(5):
    a =(x[j]*4)+10
    y.append(a)

print(y)

plt.plot(x,y)
plt.title("Custome Equation")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()

