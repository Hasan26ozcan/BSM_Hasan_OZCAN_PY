class student:
    def __init__(self,id,studentnumber,name,surname,birhdate,gender,classid):
        if(id==None):
            self.id=0
        else:
            self.id=id
        self.studentnumber=studentnumber
        self.name=name
        self.surname=surname
        self.birhdate=birhdate
        self.gender=gender
        self.classid=classid
    @staticmethod
    def createstudent(obje):
        liste=[]
        if isinstance(obje,tuple):
            liste.append(student(obje[0],obje[1],obje[2],obje[3],obje[4],obje[5],obje[6]))
        else:
            for i in obje:
                liste.append(student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return liste
    
            