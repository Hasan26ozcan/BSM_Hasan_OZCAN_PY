from heapq import merge
from numpy import inner
import pandas as pd

customers={
    "customerıd":[1,2,3,4],
    "Firstname":["ahmet","ali","hasan","canan"],
    "Lastname":["yılmaz","korkmaz","çelik","toprak"]
}


orders={
    "orderıd":[10,11,12,13],
    "customerıd":[1,2,5,7],
    "orderdate":["2010-07-04","2010-08-04","2010-07-04","2011-07-04"]
}


dforders=pd.DataFrame(orders)
print(dforders)
dfcustomer=pd.DataFrame(customers)
print(dfcustomer)
dfmerge1=pd.merge(dfcustomer,dforders,how="inner")
print(dfmerge1)
dfmerge2=pd.merge(dfcustomer,dforders,how="left")
print(dfmerge2)

dfmerge3=pd.merge(dfcustomer,dforders,how="right")
print(dfmerge3)

dfmerge4=pd.merge(dfcustomer,dforders,how="outer")
print(dfmerge4)

# bu iki dataframe arasındaki bağlatıyı saglayan tek şey customer ıd sütunudur ikiside aynı şeydir ve bu sayede
# onunla filtreleme işlemi yapmaktadır

customerA={
    "customerıd":[1,2,3,4],
    "Firstname":["ahmet","ali","hasan","canan"],
    "Lastname":["yılmaz","korkmaz","çelik","toprak"]
}


customerB={
    "customerıd":[4,5,6,7],
    "Firstname":["yağmur","çınar","cengiz","can"],
    "Lastname":["akar","toplan","yılmaz","turan"]
}


custdfa=pd.DataFrame(customerA)
custdfb=pd.DataFrame(customerB)


merges=pd.concat([custdfa,custdfb])
print(merges)
















