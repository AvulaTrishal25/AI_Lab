import math
a=int(input("enter jug a value:"))
b=int(input("enter jug b values:"))
ai=int(input("initially water in jug a:"))
bi=int(input("initially water in jug b:"))
af=int(input("final state of jug a:"))
bf=int(input("final state of jug b:"))
if a<=0 or b<=0:
    print("jug capacities must be positive.")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("negative values not allowed")
    exit(1)
def wjug(a,b,ai,bi,af,bf):
    print("list of operations:\n")
    print("1. fill jug a completely")
    print("2. fill jug b completely")
    print("3. empty jug a completely")
    print("4. empty jug b completely")
    print("5. pour from jug a till jug b is full or a becomes empty")
    print("6. por from jug b till jug a is full or becomes empty")
    print("7. pour all from jug b to jug a")
    print("8. pour all from jug a to jug b")
    while ai!=af or bi!=bf:
        op=int(input("enter operations(1-8):"))
        if op==1:
               ai=a
        elif op==2:
               bi=b
        elif op==3:
               ai=0
        elif op==4:
               bi=0
        elif op==5:
               pour_amount=min(ai,b-bi)
               ai-=pour_amount
               bi+=pour_amount
        elif op==6:
               pour_amount=min(bi,a-ai)
               bi-=pour_amount
               ai+=pour_amount
        elif op==7:
               pour_amount=min(bi,a-ai)
               ai+=pour_amount
               bi-=pour_amount
        elif op==8:
               pour_amount=min(ai,b-bi)
               bi+=pour_amount
               ai-=pour_amount
        else:
               print("invalid opeartion")
               continue
        print(f"jug a:{ai},jug b:{bi}")
        if ai==af and bi==bf:
            print("final state:jug a",ai,"jug b=",bi)
            return
    print("final state:jug a=",ai,"jug b=",bi)
gcd=math.gcd(a,b)
if(af<=a and bf<=b)and(af%gcd==bf%gcd==0):
    wjug(a,b,ai,bi,af,bf)
else:
    print("the final state is not acheivable")
    exit(1)











             
      
      

















               
