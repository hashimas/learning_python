def calc(num1, num2, operator = 'None'):
    if operator == 'None':
        return num1 + num2
    elif operator == 'addition':
        return num1 + num2
    elif operator == 'subtraction':
        return num1 - num2
    elif operator == 'division':
        return num1 / num2
    elif operator == 'multiplication':
        return num1 * num2
    else:
        return 'Invalid opetator specify'
compute = calc(3,5,'division')
print(compute)
        
        
        
        