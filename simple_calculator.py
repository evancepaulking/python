#simple calculator
def display():
    print('Please select operation-\n'\
            '1. Add\n'\
            '2. Substract\n'\
            '3. Multiply\n'\
            '4. Divide\n')

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__ == '__main__':
    display()
    choice =input('select your operation 1, 2, 3, 4 :')
    x = int(input('Enter first number : '))
    y = int(input('Enter second number : '))

    if (choice =='1'):
        print('{} + {} = {} '.format(x,y,sum(x,y)))
    elif (choice =='2'):
        print('{} - {} = {} '.format(x,y,sub(x,y)))
    elif (choice =='3'):
        print('{} * {} = {} '.format(x,y,mult(x,y)))
    elif (choice =='4'):
        print('{} / {} = {} '.format(x,y,div(x,y)))
    else:
        print('invalid input')
