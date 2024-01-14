import random
q=0
def introduce_game():
    introduce_game="""
-------------------------------------------------------------------------------------------------------
Hello There!! Welcome.
It is a Math Related game.
Rules :
        1.You will be given ten random numbers.
        2.You have 30 seconds to count them.
        3.If you can count within 60 seconds you win.Otherwise you lose.
        4.The numbers will be between 1 to 100.
        5.You just need to add.

--------------------------------------------------------------------------------------------------------
If you want to play this game then write (y=yes) and (n=no)
    """
    print(introduce_game)

def numgame(last_ans):
    for i in range(10):
        a=random.randint(1,100)
        last_ans += a
        print(a)
        if i==9:
            return last_ans
def sumans():
    print("Enter your ans : ")
    
# def comsum(ans)