'''To check whether a number is pelindrome or not and if not it prints the next pelindrome which comes after that number
Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
n=int(input('How many number you want to enter?\n'))
l=[]
for i in range(n):
    i=int(input('Enter the number\n'))
    l.append(i)

for i in l:
    if str(i)==str(i)[::-1]:
        print('This number is a Pelindrome\n')
    else:
        print(f'Opps {i} is not a pelindrome but next pelindrome is')
        while True:
            if str(i)==str(i)[::-1]:
                print(i)
                break
            else:
                i+=1
