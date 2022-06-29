#inheritance (kalıtım)


#person->name job age



class person:
    def __init__(self,firstname,lastname):
        self.firstnam=firstname
        self.lastnam=lastname
        print("person created")
    def who_am_i(self):
        print(f"you is {self.firstnam} {self.lastnam} ")
    def eat(self):
        print("ı am eating ")

class student(person):
    def __init__(self,number,firstname,lastname):
        person.__init__(self,firstname,lastname)
        self.number=number# eger burda super ile yapmıs olsaydık o zaman ya da person ikisinde aynı islevi gördugu soylenebilir
        #eski yapmıs oldugumuz yerdeki yapılandırıcıyıda kullanmasına neden olur
        print(f"ayrıyetten numara bilgisinide yazdıralım {self.number} ")

    # burda eger onceki yerden aynısını alıpta ustune yazarsak yanı eger onu degistirirsek
    #bu isleme override islemi diyoruz
    def who_am_i(self):
        person.who_am_i(self)

    def sayhello(self):
        print("say hello")
class teacher(person):
    def __init__(self, firstname, lastname,branch):
        super().__init__(firstname, lastname)
        self.branch=branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} name: {self.firstnam} lastname: {self.lastnam} ")





p1=person("ali","mehmet")
p2=student(21010310040,"mehmet","feyyaz")
t1=teacher("ahmet","soysa","engineer")

print(f" ismi:  {p1.firstnam} soyismi: {p1.lastnam} ")
print(f" ismi:  {p2.firstnam} soyismi: {p2.lastnam} ")

p1.who_am_i()
p1.firstnam
p2.who_am_i()

p1.eat()
p2.eat()
p2.sayhello()

t1.who_am_i()
