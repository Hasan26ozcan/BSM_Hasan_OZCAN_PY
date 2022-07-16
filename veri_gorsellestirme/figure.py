import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x=np.linspace(-10,9,200)
y=x**3
z=x**2
"""
figure=plt.figure()

axes_cube=figure.add_axes([0.2,0.6,0.7,0.3])
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x ekseni")
axes_cube.set_ylabel("y ekseni")
axes_cube.set_title("bu bizim isimiz1")

axes_square=figure.add_axes([0.2,0.1,0.7,0.3])

axes_square.plot(x,z,"r")
axes_square.set_xlabel("x ekseni")
axes_square.set_ylabel("y ekseni")
axes_square.set_title("bu bizim isimiz2")

plt.show()
"""
"""
figure=plt.figure()
axes=figure.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,label="cube")
axes.plot(x,z,label="square")
axes.set_xlabel("x ekseni")
axes.set_ylabel("y ekseni")
axes.set_title("ikili grafik")
axes.legend(loc=3)
# loc=1 sağ üstte çıkar
# loc =2 sol üstte çıkar
# loc =3 sol altta çıkar
# loc =4 sağ altta çıkar

plt.show()

"""

fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))
# bu (figsize )bizim açılan penceremizin boyutları olarak söyleyebiliriz
axes[0].plot(x,y,label="square")
axes[0].set_title("square")
axes[1].plot(x,z,label="cube")
axes[1].set_title("cube")
axes[0].legend()
axes[1].legend()

plt.tight_layout()
plt.savefig("figure.pdf")
plt.show()


