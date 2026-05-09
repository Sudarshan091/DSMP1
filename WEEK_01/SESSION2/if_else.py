#mujhe ek login page banana hai jisme ek predefined user id and passward hoga 
# aur uske baad mujhe use access karna pargea alag alag id se

# id = input('enter your id ')
# passward = int(input('enter your passward ')) 
# while True:
#     if id == 'sudarshan@gmail.com' and passward == 1234:
#         print('welcome sudarshan')
#     elif id == 'sudarshan@gmail.com' and passward != 1234:
#         print('wrong passward')
#     passward =input('enter passward again ')
#     if passward == '1234':
#         print('welcome sudarshan')
#     else:
#         print('wrong passward')
#         passward = input('enter passward again:')
#         if passward == '1234':
            
#             print('welcome sudarshan')
#         else:
#             print('wrong passward') 
# else:

#     print('wrong id')
   

    
# isme maine nested if else bhi use kiya hai ki jaise ki agar id sahi hai 
#lekin passward galat hai to wo mujhese phir passward mangega aur check karke response 
#generate karega     

id= str(input("enter the user id:"))
passward=int(input("enter the passward:"))
 
while True:
    if id=="sudarshan.com" and passward==1234:
        print("welcome sudarshan")
        break
    elif id=="sudarshan.com" and passward!=11234:
        print("passward is invalid")
        passward= int(input("enter the passward again"))
        if passward==1234:
            print("welcome sudarshan")
            break
        else:
            print("passward is invalid")
            passward=int(input("enter the passward again"))
            if passward==1234:
                print("welcome sudarshan")
                break
            else:
                print("passward is invalid")
                passward=int(input("enter the passward again"))
                if passward==1234:
                    print("welcome sudarshan")
                    break
                else:
                    print("passward is invalid")
                    passward=int(input("enter the passward again"))
                    if passward==1234:
                        print("welcome sudarshan")
                        break   