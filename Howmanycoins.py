


print('you have 0 coins')
answer = input('Do you want another coins? ')
answer = answer.lower() 
count = 0
while answer == 'yes':
    count +=1
    print('you have %d coin' % count)
    answer = input('Do you want another coins? ')
    
if answer == 'no':  
    print ("Bye")
