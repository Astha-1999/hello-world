text=input("enter the text")
print("original:",text)
LETTER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for key in range(len(LETTER)):
    result=""
    for symbol in text:
        if symbol in LETTER:
            num=LETTER.find(symbol)
            num=num - key
            if num < 0:
              num=num + len(LETTER)
            result=result + LETTER[num]
        else:
            result=result + symbol
print("key is %s" %(result))
