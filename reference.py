# value type => String , numbers
x=5
y=25

x=y
y=10
print(x)
print(y)

#references type => list,dizi
a =["apple","banana"]
b =["apple","banana"]
#tanımlamış olduğumuz listeyi b nin içeriğini a ya yaptığımızda ikisinde adresi aynı yer oluyor
#işte o zaman b de yaptığımız bir değişiklik otomatikmen ikisinide etkiliyor ya da a da yaptığımız bir değişikiik ikisinide 
#etkiliyor
a=b
b[0]="money"
a[0]="ı do"
#ama ikiside aynı listeyi gösteriyor yani o liste içinde yaptığımz değişiklik ikisi içinde etkiliyor
b=["orange","cherry"]
print(a)
print(b)