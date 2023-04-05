class Calc:
    def ServiceDollar(self,floyds,skin,buzz,kids,shampoo,long,mid,head,d_beard,beard):
        return round(self.Floyds(floyds),2) + round(self.Skin(skin),2) + round(self.Buzz(buzz),2) + round(self.Kids(kids),2) + round(self.Shampoo(shampoo),2) + round(self.Long(long),2) + round(self.Mid(mid),2) + round(self.Head(head),2) + round(self.dBeard(d_beard),2) + round(self.Beard(beard),2)
    def DollarHour(self,service_dollar,hours):
        return service_dollar / hours
    def Variance(self,dollar_hour):
        if dollar_hour < 49.50:
            res = 0
        else:
            res = (dollar_hour-49.50)
        return res
    def CommissionVariance(self,commission,variance):
        return commission * variance
    def Incentive(self,commission_variance,hours):
        return commission_variance * hours
    def HourlyPay(self,hours,hourly):
        return hours * hourly
    def TotalPay(self,hourly_pay,incentive):
        return hourly_pay + incentive
    
    # -- Services --
    def Floyds(self,floyds):
        return floyds * 33.00
    def Skin(self,skin):
        return skin * 38.00
    def Buzz(self,buzz):
        return buzz * 30.00 
    def Kids(self,kids):
        return kids * 23.00
    def Shampoo(self,shampoo):
        return shampoo * 6.00
    def Long(self,long):
        return long * 48.00
    def Mid(self,mid):
        return mid * 42.00
    def Head(self,head):
        return head * 43.00
    def dBeard(self,d_beard):
        return d_beard * 30.00
    def Beard(self,beard):
        return beard * 17.00
    

class ReadWrite:
    # -- Read/Write --
    def writeResult(self,file,m):
        saveFile = open(file, "a")
        saveFile.write(m)
        saveFile.close()
        return True
    def readResult(self,file):
        saveFile = open(file, "r")
        return saveFile.read()