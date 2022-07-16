
from cProfile import label
import matplotlib.pyplot as plt
"""
yil=[2011,2012,2013,2014,2015]
oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,3,5,16]
oyuncu3=[18,1,12,7,21]
# stakplot
plt.plot([],[],color="g",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")
plt.legend()
plt.title("yıllara göre gol miktarı")
plt.xlabel("yıllar")
plt.ylabel("gol miktarı")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["g","r","b"])
plt.show()

"""
"""
        pie grafic


goal_types="penaltı","kaleye atılan şut","serbest vuruş"

goals=[12,25,6]
colors=["g","y","b"]
plt.pie(goals,labels= goal_types,colors=["g","y","b"],shadow=True,explode=[0.1,0.1,0.1],autopct='%1.1f%%')
# golas grafikte kullanılacak deger
# labes isimleri goal_types
#renklerinde böyle dedik
plt.legend()
plt.show()

"""
"""
bar grafiği 0.25 ve 0.50 arasında 50 olduğunu gösterir
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="AUDİ",width=0.5)
plt.title("araç bilgileri")
plt.legend()
plt.xlabel("gün")
plt.ylabel("alınan mesafe")
plt.show()

""""""
# histogram grafiği

yaslar=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_grupları=[0,10,20,30,40,50,60,70,80,90,100]
# burda 0 ve 10 arasında kaç tane varsa o kadar çok listeyi ona göre yapıyor sayarak döndürüyor
plt.hist(yaslar,yas_grupları,histtype="bar",rwidth=(0.8))
plt.xlabel("yaş grupları")
plt.ylabel("aralık degeri")
plt.title("kaç tane")
plt.show()

"""