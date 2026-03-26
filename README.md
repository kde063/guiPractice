# 자판기 GUI구현

사용모듈 tkinter, keyboard

구상
GUI(돈 입금, 버튼 작동, 항목 추가 및 제거)

문제 및 해결
생성한 버튼이 함수를 호출할 때 모두 같은 파라미터를 가져서 출력값이 모두 같게 나옴 
```python
for i, j in enumerate(drinksDict.keys()): #generate Button
    Button(root, text=j, width=8, height=3, command=lambda: getData(j, money)).grid(row=10 , column=i+1) #파라미터 어케 날리지
```
button에 cget 메소드를 사용해서 고치고자함 -> 순서가 꼬여서 호출이 안됨 //어케하는거지
아직 안고침
