amount = float(input("Enter your amount"))
service = input("how do you like the service?")
service = service.lower() 
people = int(input('enter the number of people you want to divide on:'))
if service == 'good':
    service = amount*0.2
    print('your tip amount is ',service)
    result = service+amount
    print('The amount is' , result)
    pay = result/people
    print ('you will pay:', pay)

if service == 'fair':
    service = amount*0.15
    print('your tip amount is ',service)
    result = service+amount
    print('The amount is' , result)
    pay = result/people
    print ('you will pay:', pay)
if service == 'bad':
    service = amount*0.1
    print('your tip amount is ',service)
    result = service+amount
    print('The amount is' , result)
    pay = result/people
    print ('you will pay:', pay)
