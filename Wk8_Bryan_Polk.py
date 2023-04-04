# Program Name: Wk8_Bryan_Polk.py
# Student Name: Bryan Polk
# Course: ENTD220
# Instructor: Sammy Abaza
# Date: 28 Mar 2023
# Copy Wrong: This is my work

# -- Import week 8 library --
import Wk8_Bryan_Polk_Mylib as w8l

# Intro

print("Hello, welcome to my calculator!")
print('This program will take low-end and high-end inputs from you as well ')
print('as two numbers that you would like to run through selected equations.')
print('The program will then check that your numbers are within your selected')
print('ranges and send them through select equations.')

 # Dynamic Class Objects
obj0 = w8l.checkRange()
obj1 = w8l.calculator()
obj2 = w8l.calculator()
obj3 = w8l.calculator()
obj4 = w8l.calculator()
# --Main program--
while True:

    # Testing user input ranges
    try:
        lr = float(input("--> Please enter lower range: "))
        hr = float(input("--> Please enter higher range: "))

        # Testing user input numbers
        n1 = float(input("--> Please enter first number: "))
        n2 = float(input("--> Please enter second number: "))

        # Equations
        if obj0.checkn(lr, n1, hr) and obj0.checkn(lr, n2, hr):

            # -- Menu Selections --
            myDict = {'1 -': 'Add numbers',
                      '2 -': 'Subract numbers',
                      '3 -': 'Mulitply numbers',
                      '4 -': 'Divide numbers',
                      '5 -': 'Scalc',
                      '6 -': 'All-in-one',
                      '7 -': 'Exit program.'}
            for item in myDict.keys():
                print(item, myDict[item])

            # -- Menu selection outputs --
            selection = input('Please Choose a menu option: ')
            while selection != '7':
                if selection == '1':
                    print(n1, "+", n2, "=", round(obj1.add(n1,n2), 2))
                    x = str(n1)+"+"+str(n2)+"="+str(obj1.add(n1,n2))+"\n"
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                        break
                    

                elif selection == '2':
                    print(n1, "-", n2, "=", round(obj1.sub(n1,n2), 2))
                    x = str(n1)+"-"+str(n2)+"="+str(obj1.sub(n1,n2))+"\n"
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                        break

                elif selection == '3':
                    print(n1, "*", n2, "=", round(obj1.multiply(n1,n2), 2))
                    x = str(n1)+"*"+str(n2)+"="+str(obj1.multiply(n1,n2))+"\n"
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                        break

                elif selection == '4':
                    print(n1, "/", n2, "=", round(obj1.divide(n1, n2), 2))
                    x = str(n1)+"/"+str(n2)+"="+str(obj1.divide(n1,n2))+"\n"
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                        break

                elif selection == '5':
                    calc_string = input("Calc string in this format; value1, value2, operator -> ")
                    x = str(obj2.scalc(calc_string))
                    print(obj2.scalc(calc_string))
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                        break

                elif selection == '6':
                    dictAIO = dict(obj3.aio(n1, n2))
                    for item in dictAIO.keys():
                        print(item, dictAIO[item])
                        x = str(dict(obj3.aio(n1, n2)))+"\n"
                    save = input("save results? y/n: ")
                    if save == "y":
                        obj4.writeResult("results.txt",x)
                    else:
                       break

                else:
                    print('Invalid option.')
                    break

        else:
            print("Numbers are not in range.")

        # --Restart program--
        restart = input("More calculations? y/n: ")
        if restart == "y":
            continue
        else:
            break

    # Exception - one used for keyboard interrupt and the other for invalid inputs (non-numerical)
    except KeyboardInterrupt:
        print("You used Ctrl+C to end the program.")
    except Exception as e:
        print("Error -->", e)
    continue
print("-- Calculation results --","\n")
print(obj3.readResult("results.txt"))
print('Thank you for using my calculator.')
