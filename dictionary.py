#key -value

# 41 => kocaeli 34 =>istanbul

sehirler=["kocaeli","istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index("kocaeli")])


plakalar={"kocaeli": 41,"istanbul":34 }
          # key     value

print(plakalar["istanbul"])
plakalar["ankara"]=6
print(plakalar)
plakalar["ankara"]=100
print(plakalar)

users={
    "sadikturan" : {
        "age": {
            56,67,89
        },
        "para":{
            123,1234,321,
        },
        "roles":["admin","users"],
        # yani burdada olduğunu gibi içinde dizileri kullanabiliyoruz ve ayrıyetten
        #eğer isteseydik tekrarda bir "{}" yapar devam da ettirtebilirdik


    } ,
    "cınarturan" : 2 ,

}
print(users)
print(users["sadikturan"]["para"])
print(users["sadikturan"]["roles"][0])

