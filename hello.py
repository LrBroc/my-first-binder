import numpy as np
import matplotlib.pyplot as plt

print("Hello from Binder!")

x = np.linspace(0,3.1415927,num=100)
y = np.sin(x)
plt.plot(x,y,'b-')
plt.savefig('figure.pdf',format = 'pdf')
plt.show()
