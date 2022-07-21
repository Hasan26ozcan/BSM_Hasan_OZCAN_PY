class Class:
    def __init__(self,id,name,teacherıd):
        if(id==None):
            self.id=0
        else:
            self.id=id
        self.name=name
        self.teacherıd=teacherıd
    @staticmethod
    def createclass(list):
        liste=[]

        for i in list:
            liste.append(Class(i[0],i[1],i[2]))
        return liste

