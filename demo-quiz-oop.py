#Questions

import this


class questions:
    def __init__(self,text,choices,answer):#burda sorumuzu şıkalarımızı ve doru cevabımızı giriyoruz
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkanswer(self,youanswer):
         return self.answer==youanswer

p1=questions("en iyi programlama dili nedir ?",["c#", "java", "python", "javascript" , "go"] , "python" )
p2=questions("en popüler programlama dili nedir ?",["c#",  "python","java", "javascript" , "go"] , "python" )
p3=questions("en çok kazandıran programlama dili nedir ?",[ "python", "javascript" ,"c#", "java", "go"] , "python" )


bol1=p1.checkanswer("java")
bol2=p2.checkanswer("python")
bol3= p3.checkanswer("go")
print(bol1)
print(bol2)
print(bol3)

#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionsindex=0
    def getquestions(self):
        return self.questions[self.questionsindex].text
    def displayquestions(self):
        this =self.questions[self.questionsindex]
        print(f"soru {self.questionsindex+1} : {this.text}  ")
        for x,y in  enumerate(this.choices):
            print(f"{x+1}:) {y} ")
        answer=int(input())
        self.guess(answer)
        self.loadquestions()        
    def guess(self,answer):
        this=self.questions[self.questionsindex]
        answers= this.choices[answer-1]
        if(this.checkanswer(answers)):# buraya dikkat etmemiz gerek eger burada deger true ya da false gelirken sikinti 
                                     # cikiyorsa o zaman yapmamiz gereken tekrardan bir metot kullanmak
            self.score+=1
        self.questionsindex+=1


    def loadquestions(self):
        if(len(self.questions)==self.questionsindex):
            self.showscore()
        else:
            self.displayprogress()
            self.displayquestions()
    def showscore(self):
        print(f"score: {self.score} ")
    def displayprogress(self):
        totalnumber=len(self.questions)
        questionnumber=self.questionsindex+1

        if(questionnumber>totalnumber):
            print("quiz bitti")
        else:
            print(f"quesstion  {questionnumber} of {totalnumber} ".center(100,"*"))



    
p1=questions("en iyi programlama dili nedir ?",["c#", "java", "python", "javascript" , "go"] , "python" )
p2=questions("en popüler programlama dili nedir ?",["c#",  "python","java", "javascript" , "go"] , "python" )
p3=questions("en çok kazandıran programlama dili nedir ?",[ "python", "javascript" ,"c#", "java", "go"] , "python" )
p4=questions("en çok kazandıran programlama dili nedir ?",[ "python", "javascript" ,"c#", "java", "go"] , "python" )
p5=questions("en kolay kazandıran programlama dili nedir ?",[ "python", "javascript" ,"c#", "java", "go"] , "python" )


questions=[p1,p2,p3,p4,p5]

quiz=Quiz(questions)

quiz.loadquestions()
#burda bu metotdan başlaması sayesinde ekrana yazdırma isleminde kacıncı soruda oldugu falanda gozukuyor






