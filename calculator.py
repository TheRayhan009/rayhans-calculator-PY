# a,sine,b=map(str,input().split())
# x=int (a)
# y=int (b)
# if sine=="+":
#     print("Ans ->",x+y)
# elif sine=="-":
#     print("Ans ->",x-y)
# elif sine=="x":
#     print("Ans ->",x*y)
# elif sine=="/":
#     print("Ans ->",x/y)
# elif sine=="^":
#     print("Ans ->",x**y)
# elif sine=="%":
#     print("Ans ->",x%y)

from pak import calculator as af

af.rul()
af.want()
input1 = int(input())
#a, sine, b = map(str, input().split())
#ans = af.calculator(a, sine, b, ans=0)
ans=0
for _ in range(input1):
    sine, b = map(str, input().split())
    ans=ans+af.calculator2(sine, b, ans=0)

print("Final result:", ans)
