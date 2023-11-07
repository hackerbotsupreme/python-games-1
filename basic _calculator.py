# define the functions needed to calculate add, sum , multiplication , division 
# print options to the user 
# ask for for the values 
# call the functions 
# while loop to cintinue untill the user want to exit 



# and one more thing is that 
# i used to believe that computer always represents numbers as float by default so 
# i was wrong it doesnot and its case specific 

def add(a,b):
    answer= (a+b)  # note one thing that by doing it in this way we dont have to convert it into the int later 
    return print( (str(a)+'+'+str(b)+'='+str(answer)+'\n'))  # concatination 
def sub(a,b):
    answer=(a-b)
    return print(str(a)+'-'+str(b)+'='+str(answer)+'\n')# \n will add a new line to the end end of one program and before another program ends 
def mul(a,b):
    answer=a*b
    return print(str(a)+'*'+str(b)+'='+str(answer)+'\n')
def div(a,b):
    answer=a/b
    return print(str(a)+'/'+str(b)+'='+str(answer)+'\n')
while True :# what this will do is it will continue calculating untill i call the quit function that is E.
    print('A ',' Addition ')
    print('B','subtraction')
    print('c','multiplication')
    print('D', 'Division')
    print('E','exit ')
    choice=input('input your choice :')


    if choice == 'A' or choice == 'a':
        print('Addition')
        a=int(input('input first number : '))
        b=int(input('input second  number : '))
        add(a,b)
    elif choice == 'B' or choice == 'b':
        print('subtraction')
        a=int(input('input first number : '))
        b=int(input('input second  number : '))
        sub(a,b)
    elif choice == 'C' or choice == 'c':
        print('Multiplication')
        a=int(input('input first number : '))
        b=int(input('input second  number : '))
        mul(a,b)
    elif choice == 'D' or choice == 'd':
        print('division')
        a=int(input('input first number : '))
        b=int(input('input second  number : '))
        div(a,b)
    elif choice == 'E' or choice == 'e':
        print('program ended ')
        quit()
# quit() function says exit  the  program .











