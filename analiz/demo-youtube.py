import pandas as pd


data=pd.read_csv("youtube-ing.csv")
df=pd.DataFrame(data=data)

#1- ilk 10 kaydı getiriniz
print(df.head(10))
#2- ikinci 5 kaydı getiriniz
print(df.loc[5:10,:])
#3- Dataset'de bulunan kolon isimleri ve sayısını bulunuz
print(df.columns)
print(len(df.columns))
#4- aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz
#(thumbnail_link,comments_disabled,raiting_disable,video_error_or_removed,description)
df.drop("comments_disabled",axis=1,inplace=True,)
df.drop("thumbnail_link",axis=1,inplace=True,)
df.drop("ratings_disabled",axis=1,inplace=True,)
df.drop("video_error_or_removed",axis=1,inplace=True,)
df.drop("description",axis=1,inplace=True,)
print(df)
print(len(df.columns))
#5- beğenme(like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz
likemean=df["likes"].mean()
dislikemean=df["dislikes"].mean()
print(likemean)
print(dislikemean)
#6- ilk 50 videonun like ve dislike kolonlarını getiriniz
result=df.head(50)
results=result[["likes","dislikes"]]
print(results)

#7- en çok görüntülenen video hangisidir
result=df["views"].max()
print(result)
lsite=df.groupby("views").get_group(result)
print(lsite["title"].iloc[0])




#8- en düşük görüntülenen video hangisidir
result=df["views"].min()
print(result)
lsite=df.groupby("views").get_group(result)
print(lsite["title"].iloc[0])



#9- en fazla görüntülenen ilk 10 video hangisidir
result=df.sort_values("views",ascending=False)

print(result["title"].head(10))





#10- kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz



result=df.groupby("category_id")["likes"].mean()
print(result.sort_values(ascending=False))




#11- kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız




result=df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)
print(result)





#12- her kategoride kaç video vardır





result=df.groupby("category_id")["video_id"].count().sort_values()
print(result.sort_values(ascending=False))






#13- her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz





result=df["title"].str.len()
df["title_len"]=result
print(df)





#14- her video için kullanılan tag sayısını yeni kolonda gösteriniz




print(df["tags"])
df["tag_counter"]=df["tags"].apply(lambda x: x.split("|")).str.len()


print(df["tag_counter"])

def tagcount(tag):
    return tag.split("|")

df["tag_count"]=df["tags"].apply(tagcount).str.len()

print(df)

#15- en popüler videoları listeleyiniz (like/dislike oranına göre)



# by benim yaptığım yıldızdan sonrası hocanın yaptığı olarak ayrılıyor
result=df[["likes","dislikes"]]
print(result)
result=result["likes"]/(result["dislikes"]+result["likes"])
print(result)

df["likes/dislikes"]=result

df=df.sort_values("likes/dislikes",ascending=False).dropna(how="any")[["title","likes","dislikes","likes/dislikes"]]
print(df)
print(df.groupby(["likes/dislikes"]).get_group(1)["likes"].max())# buda popülaritesi en yüksek olan video deyebiliriz
# çünkü en fazla like bunda var 
#--***************************************************************--------------------
def likesdislikes(dataset):
    likes=list(dataset["likes"])
    dislikes=list(dataset["dislikes"])

    liste=zip(likes,dislikes)
    cevap=[]

    for like,disli in liste:
        if(like+disli)==0:
            cevap.append(0)
        else:
            cevap.append(like/(disli+like))
    return cevap

df["begeni_oranı"]=likesdislikes(df)

df=(df.sort_values("begeni_oranı",ascending=False))
print(df[["likes","dislikes","title"]].head(10))
    
















