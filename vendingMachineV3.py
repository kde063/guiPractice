from tkinter import *
from keyboard import *

root = Tk()
root.geometry("400x400")

drinksDict = {"orange" : 1400, "soda" : 1800, "coke" : 1800, "water" : 500} #button List
buttonDict = {} #key:name value:Button
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
        print("잔액 부족")


def validate(P):
    if len(P) == 0:
        return True
    elif P == "." or P.isdigit():
        return True
    else:
        return False

def buttonCommand():
    global money
    try:
        money = int(inpEntry.get())
    except:
        print("입력해주세요")

def generateButton():
    for i, j in enumerate(drinksDict.keys()): #generate Button
        temp = Button(root, text=j, width=8, height=3, command=lambda: getData(j, money)) #파라미터 어케 날리지
        temp.grid(row=10 , column=i+1)
        buttonDict[j] = temp

def removeButton():
    for i in buttonDict.values():
        print(type(i))
        i.destroy()

def adminPage():
    print("관리자 모드")
    while(1):
            action = input("추가 / 삭제 / 종료\n").strip()

            if(action == "추가"):
                addDrink = input("추가할 음료수 이름: ")
                addPrince = input("추가할 음료수 가격: ")

                if(addDrink in drinksDict):
                    print("이미 존재합니다")
                else:
                    drinksDict[addDrink] = addPrince

            elif(action == "삭제"):
                delDrink =  input("삭제할 음료수 이름: ")
    
                if(delDrink in drinksDict):
                    del(drinksDict[delDrink])

                else:
                    print("존재하지 않습니다")

            elif(action == "종료"):
                removeButton()
                generateButton()
                break
            else:
                print("오류")

add_hotkey("ctrl+a+b", lambda: adminPage())

#########################################################################################
vcmd = (root.register(validate), '%P')

inpEntry = Entry(root, width=10, validate = "key",validatecommand=vcmd)
inpEntry.grid(row=1 , column=1)

moneyButton = Button(root, width=3, command=buttonCommand, text="완료").grid(row=1 , column=2)

generateButton()

root.mainloop()
