try:
    print('Welcome to the ATM')
    t_money=int(input('Enter the amount in your Bank:'))
    pin=int(input('Enter the PIN:'))
    print('1.check balance')
    print('2.Deposit money')
    print('3.Withdraw money')
    print('4.Exit')
    n=int(input('Enter your choice(1,2,3,4):'))
    p=int(input('Enter your PIN:'))
    if p==pin:
        if n==1:
            print('Your balance is :',t_money)
        elif n==2:
            deposit_money=int(input('Enter the amount:'))
            t_money+=deposit_money
            print('Your total balance is :',t_money)
        elif n==3:
            withdraw_money=int(input('Enter the amount:'))
            if withdraw_money>t_money:
                print('Insufficient balance')
                print('Your balance is :', t_money)
            else:
                t_money-=withdraw_money
                print('Your total balance is :',t_money)
        elif n==4:
            exit
        else:
            print('Invalid option')
    else:
        print('Incorrect PIN')
    print('Thank you for visit ATM')
except ValueError:
    print('Enter valid data')