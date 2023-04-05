import Pay_CalculatorLib as lib

obj0 = lib.Calc()
obj1 = lib.ReadWrite()

# -- Main --
while True:
    # -- User Inputs --
    floyds = float(input("Floyds cuts: "))
    skin = float(input("Skin fades: "))
    buzz = float(input("Buzz cuts: "))
    kids = float(input("Kids cuts: "))
    shampoo = float(input("Shampoos: "))
    long = float(input("Long Layers: "))
    mid = float(input("Mid-lengths: "))
    head = float(input("Head shaves: "))
    d_beard = float(input("Detailed beard trims: "))
    beard = float(input("Beard trims: "))

    # -- Auto Calculations --
    hours = float(input("Hours worked after lunches: "))
    commission = float(input("Commission percentage in decimal form: "))
    hourly = float(input("Hourly wage: $"))

    # -- Metric Calculations --
    service_dollar = obj0.ServiceDollar(floyds,skin,buzz,kids,shampoo,long,mid,head,d_beard,beard)
    print("Total service dollars = $",round(service_dollar,2))
    dollar_hour = obj0.DollarHour(service_dollar,hours)
    print("Service dollars per hour = $",round(dollar_hour,2))
    variance = obj0.Variance(dollar_hour)
    print("Service dollar variance = $",round(variance,2))
    commission_variance = obj0.CommissionVariance(commission,variance)
    print("Commission variance = $",round(commission_variance,2))
    incentive = obj0.Incentive(commission_variance,hours)
    print("Production incentive = $",round(incentive,2))
    hourly_pay = obj0.HourlyPay(hours,hourly)
    print("Your hourly earnings are = $",round(hourly_pay,2))
    gross_pay = obj0.TotalPay(hourly_pay,incentive)
    print("Total pay = $",round(gross_pay,2))

    x = "\n" "\n" "--Results--" "\n"  "Service Dollar total = $" +str(service_dollar)+ "\n" "Hours Worked - " +str(hours)+ "\n" "Dollar/Hour = $" +str(dollar_hour)+ "\n" "Variance = $" +str(variance)+ "\n" "Commission Variance = $" +str(commission_variance)+ "\n" "Production Incentive = $" +str(incentive)+ "\n" "Hourly Pay = $" +str(hourly_pay)+ "\n" "Gross Pay = $" +str(gross_pay)

    save = input("save results? y/n: ")
    if save == "y":
        obj1.writeResult("results.txt",x)
    else:
        break
    
    restart = input("More calculations? y/n: ")
    if restart == "y":
        continue
    else:
        break
# --Restart program--
while True:
    restart = input("More calculations? y/n: ")
    if restart == "y":
        continue
    else:
        break
print("-- Calculation results --","\n")
print(obj1.readResult("results.txt"))