import matplotlib.pyplot as plt
import numpy as np


# x=[0,1,2,3,4]
# y=[0,1,4,9,16]
# plt.plot(x,y,color="red",linewidth="5")
# plt.plot(y,x,"^--r")
# # ilk verilen bizim x eksenimiz ikinci verilen y eksenimiz
# plt.axis([0,10,0,30])# burda ilk 0 10 x sonraki 0 30 y ekseni için dir 
# # burda ise önemli olan x ve y ekseninde uzunluğuunun nereye kadar gideceğidir
# plt.title("grafik başlığı")
# plt.xlabel("xlabel")
# plt.ylabel("ylabel")


# plt.show()# sistemi açmak için kullandığımız birşey

# şimdi farklı bir örnke daha yapalım

# x=np.linspace(0,2,100)
# plt.plot(x,x,label="lineer",color="red")
# plt.plot(x,x**2,label="quadratic",color="yellow")
# plt.plot(x,x**3,label="cubig",color="black")
# plt.title("x garifğimiz")
# plt.xlabel("x alanı")
# plt.ylabel("y alanı")
# plt.legend()# grafikte neyin ne olduğunu görmemizi saglıyor
# plt.show()

# bir tane daha grafik

# x=np.linspace(0,2,100)

# fig,axs=plt.subplots(3)
# axs[0].plot(x,x,color="red")
# axs[0].set_title("linear")
# axs[1].plot(x,x**2,color="yellow")
# axs[1].set_title("quadractad")
# axs[2].plot(x,x**3,color="green")
# axs[2].set_title("cubiq")
# plt.tight_layout()

# # eger üst üste çizmek stersek aynı adres mantığı gibi dşünüp aynı alana plot yaparak aynı alana
# # çizmesini sağlayabiliriz
# plt.show()

# başka bir grafik örneği bunda ise normal alt alta değil tablo şekilde grafik koyucaz
# x=np.linspace(0,2,100)

# fig,axs=plt.subplots(2,2)
# fig.suptitle("Grafik Baslıgı")
# axs[0][0].plot(x,x,color="red")
# axs[0][1].plot(x,x**2,color="green")
# axs[1][0].plot(x,x**3,color="black")
# axs[1][1].plot(x,x**4,color="yellow")

# plt.show()

import pandas as pd

df=pd.read_csv("nba.csv")
df=df.drop("Number",axis=1)
print(df)
print(df.columns)
result=df.groupby("Team").mean()
result.plot(subplots=True)# eger result tan sonra head yapsaydık o zaman ilk 5 tanesi için grafik çalışırdı
plt.legend()
plt.tight_layout()
plt.show()








