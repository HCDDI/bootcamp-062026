
try:
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    print("i am try just started")
    if b%2 == 0:
        raise Exception
    else:
        print(a/b)
        print("i am try,i am done")

    
except Exception as e:
     print("division by evens are not allowed")
else:
         print("hi am else now alive because try is excuted.")
finally:
    print("code excuted")