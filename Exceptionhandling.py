#Exception handling

print("1")
a=int(input("a: "))
b=int(input("b: "))
try:
    print(a/b)
except:
    print("Error")    
finally:
    print("Thankyou")  

print("2")
a=int(input("a: "))
b=int(input("b: "))
try:
    print(a/b)
except Exception as e:
    print(f"Error occured: {e}")   
finally:
    print("program ended!")       
    
print("3")
a=int(input("a: "))
b=int(input("b: "))      
try:
    print(a/b)  
except Exception as e:
    print(f"Error occured :{e}")    
    b = int(input("Enter the num: "))
    print(a/b)
finally:
    print("Mugitu")    

try:
    a= int(input("a: "))
    print(10/a)
except ZeroDivisionError:
    print("ok")
finally:
    print("Nodana")    

try:
    boy = input("who do you want to marry?: ")
    if boy.lower() != "darshan":
        raise Exception("you can only marry Darshan")
except Exception as e:
    print(f"Error : {e}")    
else:
    print("yes! Darshan is ready to marry you")    