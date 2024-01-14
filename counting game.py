from pak import pakcounting as me
import time
import os
me.introduce_game()
yesorno=input()
last_ans=0
q=0
if yesorno=="y":
    print("\n")
    c=me.numgame(last_ans=0)
    print("\n"+"Time starts Now!!")
    for j in range(1,61):
        time.sleep(1)
        #os.system("cls")
        print(j)
        
    me.sumans()
    ans=int(input())
    if ans == c:
        print("YES!! YOU GOT IT..")
    else:
        print("WRONG ANS.."+"The ans was : ",c)
else:
    print("Have a good day Bye..")