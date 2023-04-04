# Program Name: Wk8_Bryan_Polk_Mylib.py
# Student Name: Bryan Polk
# Course: ENTD220
# Instructor: Sammy Abaza
# Date: 28 Mar 2023
# Copy Wrong: This is my work

# --Range Check--
class checkRange():
    def checkn(self,lr,n,hr):
        return lr <= n <= hr

# --Equations--
class calculator():
    def add(self,n1,n2):
        return n1 + n2
    def sub(self,n1,n2):
        return n1 - n2
    def multiply(self,n1,n2):
        return n1 * n2
    def divide(self,n1,n2):
        return n1 / n2
    def aio(self,n1,n2):
        return {'Addition = ':round(self.add(n1,n2),2) ,'Subraction = ':round(self.sub(n1,n2),2) ,'Multiplication = ':round(self.multiply(n1,n2),2) ,'Division = ':round(self.divide(n1,n2),2)}
    def scalc(self,p):
            lstring=p.split(",")
            if lstring[2]=="*":
                res= self.multiply(int(lstring[0]),int(lstring[1]))
            if lstring[2]=="+":
                res= self.add(int(lstring[0]),int(lstring[1]))
            if lstring[2]=="/":
                res= self.divide(int(lstring[0]),int(lstring[1]))
            if lstring[2]=="-":
                res= self.sub(int(lstring[0]),int(lstring[1]))
            return res
    # -- Read/Write --
    def writeResult(self,file,m):
        saveFile = open(file, "a")
        saveFile.write(m)
        saveFile.close()
        return True
    def readResult(self,file):
        saveFile = open(file, "r")
        return saveFile.read()
'''# --Scalc--
class staticCalc():
    def scalc(self,p):
        lstring=p.split(",")
        if lstring[2]=="*":
            res= calculator.multiply(self,int(lstring[0]),int(lstring[1]))
        if lstring[2]=="+":
            res= calculator.add(self,int(lstring[0]),int(lstring[1]))
        if lstring[2]=="/":
            res= calculator.divide(self,int(lstring[0]),int(lstring[1]))
        if lstring[2]=="-":
            res= calculator.sub(self,int(lstring[0]),int(lstring[1]))
        return res

# -- All-in-one --
class AIO():
    def aio(self,n1,n2):
        return {'Addition = ':round(calculator.add(self,n1,n2),2) ,'Subraction = ':round(calculator.sub(self,n1,n2),2) ,'Multiplication = ':round(calculator.multiply(self,n1,n2),2) ,'Division = ':round(calculator.divide(self,n1,n2),2)}
'''