import operator
import math
import cmath
import functools as fc





def main():
    q=True
    while(q):
        s1="\n\n1)For Addition ,Subtraction ,Multiplication ,Division ,Mod\n"
        s2="2)To find square root or exponent\n"
        s3="3)For Trigonometric calculations\n"
        s4="4)For conversion between Degree and Radian  \n \t\t Select any(1/2/3/4):--> "
        
        t = int(input(s1+s2+s3+s4))

        if(t==1):
            t1 = input("a)Addition\nb)Subtraction\nc)Multiplication\nd)Division\ne)Mod\n Select any(a/b/c/d/e):--> ")

            if(t1=="a"):
                print("\n\tADDITION :")
                print("Enter all the numbers separated by a space ")
                add = list(map(float,input().split()))
                print("Result is : ",sum(add))

            elif(t1=="b"):
                print("\n\tSUBTRACTION :")
                print("Enter all the numbers separated by a space ")
                subt = list(map(float,input().split()))
                r=fc.reduce(operator.sub ,subt)
                print("Result is : ",r)

            elif(t1=="c"):
                print("\n\tMULTIPLICATION :")
                print("Enter all the numbers separated by a space ")
                mult = list(map(float,input().split()))
                print("Result is : ",math.prod(mult))


            elif(t1=="d"):
                print("\n\tDIVISION :")
                print("Enter all the numbers separated by a space ")
                div = list(map(float,input().split()))
                first =div.pop(0)
                for i in div:
                    first/=i

                print("Result is : ",first)


            elif(t1=="e"):
                print("\n\tMOD :")
                print("Enter all the numbers separated by a space ")
                mod = list(map(float,input().split()))
                first =mod.pop(0)
                for i in mod:
                    first%=i

                print("Result is : ",first)

            else:
                print("Sorry, please select correct option")
                
                
        elif(t==2):
            t2=input("\na)Square Root\nb)Exponent\n Select any(a/b):--> ")

            if(t2=="a"):
                print("\n\tSQUARE ROOT :")
                sq= float(input("Enter the number : "))
                print("Result is : ",cmath.sqrt(sq))

            elif(t2=="b"):
                print("\n\tEXPONENT :")
                m,n= map(float,input("Enter two numbers separated by a space : ").split())
                print("Result is : ",math.pow(m,n))

            else:
                print("Sorry, please select correct option")

        elif(t==3):
            print("\n\tTRIGONOMETRIC FUNCTION :")
            t3=input("\na)For sine\nb)For cosine\nc)For tangent Select any(a/b/c):--> ")
            arg =float(input("Enter the value in radian : "))
            if(t3=="a"):
                print("SINE of ",arg," is : ",math.sin(arg))
            elif(t3=="b"):
                print("COSINE of ",arg," is : ",math.cos(arg))

            elif(t3=="c"):
                print("TANGENT of ",arg," is : ",math.tan(arg))
            else:
                print("Sorry, please select correct option")


        elif(t==4):
            t4=input("\na)Radian to Degree\nb)Degree to Radian\n Select any(a/b):--> ")

            if(t4=="a"):
                rtd =float(input("Enter value in radian : "))
                print("Radian to Degree : ",math.degrees(rtd))

            elif(t4=="b"):
                dtr =float(input("Enter value in radian : "))
                print("Degree to Radian : ",math.radians(dtr))

            else:
                print("Sorry, please select correct option")



        else:
            print("Sorry, please select correct option")



        quits=input("\nIF YOU WANT TO EXIT PRESS (ANY_KEY+ENTER) ELSE PRESS ENTER.......")
        if(quits==""):
            q= True
        else:
            q=False
        
                
                

                
            
                

                
                
            

            

                
                

            
                
                

                
                
                
                
                
                
                
                







if _name_ == "_main_":
    main()