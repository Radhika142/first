a=int(input('Enter first no='))
b=int(input('Enter second no='))
c=int(input('Enter third no='))
if a==b==c:
    print('no are equal')
elif (a==b)>c:
    print('a and b are equal and greater than c')  
elif (a==c)>b:
    print('a and c are equal and greater than b')  
elif (b==c)>a:
    print('c and b are equal and greater than a')   
elif a>b>c:
    print('a is greater ')     
elif b>a>c:
    print('b is greater ')    
elif c>b>a:
    print('c is greater ')                                            