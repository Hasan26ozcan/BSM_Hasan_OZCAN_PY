import pandas as pd

df= pd.read_csv("imdb.csv")
print(df)
#1- dosyada hakkındaki bilgiler
print(type(df))
print(df.columns)# birde kolonlaırn başlıklarını koyuyo
print(df.info())# bize bilgii getirir
#2- ilk 5 kaydı gösterin
firstfive=df.head(5)
print(firstfive)
#3- ilk 10 kaydı gösterin
firstten=df.head(10)
print(firstten)
#4- son 5 kaydı gösterin
lastfive=df.tail(5)
print(lastfive)
#5- son 10 kaydı gösterin
lastten=df.tail(10)
print(lastten)
#6- sadece Movie_Title kolonunu alın.
Movie_Titlecolumns=df.loc[:,"Movie_Title"]
print(Movie_Titlecolumns)
#7- sadece Movie_Title kolonunu içeren ilk 5 kaydı alın
firstfivemovietitle= df.loc[:,"Movie_Title"].head()
print(firstfivemovietitle)
#8- sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın
firstmovietitlerating=df.loc[:,["Movie_Title","Rating"]].head(5)
print(firstmovietitlerating)
#9- sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
lastmovietitlerating=df.loc[:,["Movie_Title","Rating"]].tail(7)
print(lastmovietitlerating)
#10- sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın
secondfivelist=df.loc[5:10,["Movie_Title","Rating"]]
print(secondfivelist)

#11- sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alınız
s=df.loc[:,"Rating"]>=8.0
first50puan8=df[s].head(50)
screanwrite=first50puan8.loc[:,["Movie_Title","Rating"]]
print(screanwrite)

#12- yayın tarihi 2014 ile 2015 arasında olan filsmlerin isimlerini getiriniz

years=df.loc[:,"YR_Released"]
print(years)
cor=(years>=2014.0) & (years<=2015.0)
movielist= df[cor]
print(movielist)
moviename=movielist.loc[:,"Movie_Title"]
print(moviename)



#13- değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#       8 ile 9 arasında olan filmleri listeleyiniz

sayi=df.loc[:,"Num_Reviews"]
control1=df.loc[:,"Rating"]
degerlendirme=(sayi>100000) | ((control1>8.0)&(control1<9.0))
print(df[degerlendirme])

