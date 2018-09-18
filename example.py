from math import sqrt
print('Welcome to Stetis ATM Machine \n')
print('[1] Withdrawal\t\t\t[2] Balance \n[3] Transfer \t\t\t[4] Airtime')
x = int(input('Enter your selection option number \n'))
if x == 1:
    amount = int(input('Enter the amount you want to withdraw\n'))
    if amount < 10000:
        print('\nYou withdrew ',amount)
        print('\nYour remaining balance = ',10000 - amount)
        print('\nDo you want to perfrom another transanction ? Y/N ')
    else:
            print('Insufficient amount! ')
if x == 2:
    print('You account balance = 10000.00')

def withdrawal(args):{
    
}
    
    

    