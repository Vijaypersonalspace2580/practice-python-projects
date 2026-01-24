print('Welcome to password strength checker')
p=input('enter your password=')
length=len(p)
if length>=6:
    capital=0
    small=0
    special=0
    number=0
    for i in p:
        if(i.isupper()==True):
            capital+=1
        elif(i.islower()==True):
            small+=1
        elif(i.isdigit()==True):
            number+=1
        else:
            special+=1
    if(capital>0 and small>0 and number>0 and special>0):
        print('password is strong')
    else:
        print('Invalid password')
        if(capital==0):
            print('There is no capital letter in password')
        if(small==0):
            print('There is no small letter in password')
        if(number==0):
            print('There is no number letter in password')
        if(special==0):
            print('There is no special character in password')
else:
    print('Invalid password')
    print('password contain minimum 6 characters')
print('Thank you for visit password strength checker')