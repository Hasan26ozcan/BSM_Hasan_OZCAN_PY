class teacher:
    def __init__(self,id,bransh,name,surname,birhdate,gender):
        if(id==None):
            self.id=0
        else:
            self.id=id
        self.bransh=bransh
        self.name=name
        self.surname=surname
        self.birhdate=birhdate
        self.gender=gender
