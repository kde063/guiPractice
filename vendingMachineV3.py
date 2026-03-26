from tkinter import *

root = Tk()
root.geometry("400x400")

drinksDict = {"orange" : 1400, "soda" : 1800, "coke" : 1800, "water" : 500} #button List
money = 0

def getData(drink, money):
    drink = drink
    money = money

    if(drink in drinksDict.keys()):
        value = drinksDict[drink]

    if (value <= money):
        money -= value
        print(f"{drink}나옴")
    else:
        print("오류")


def validate(P):
    if len(P) == 0:
        return True
    elif P == "." or P.isdigit():
        return True
    else:
        return False

def buttonCommand():
    global money
    money = int(inpEntry.get())

def adminPage():
    pass

#########################################################################################
vcmd = (root.register(validate), '%P')

inpEntry = Entry(root, width=10, validate = "key",validatecommand=vcmd)
inpEntry.grid(row=1 , column=1)

moneyButton = Button(root, width=3, command=buttonCommand, text="완료").grid(row=1 , column=2)

for i, j in enumerate(drinksDict.keys()): #generate Button
    #print(j)
    Button(root, text=j, width=8, height=3, command=lambda: getData(j, money)).grid(row=10 , column=i+1) #파라미터 어케 날리지


root.mainloop()