amount = float(input("Enter your amount"))
service = input("how do you like the service?")
service= service.lower() 
if service == 'good':
    service = amount*0.2
    print('your tip amount is ',service)
    result = service+amount
    print('You need to pay' , result)
if service == 'fair':
    service = amount*0.15
    print('your tip amount is ',service)
    result = service+amount
    print('You need to pay' , result)
if service == 'bad':
    service = amount*0.1
    print('your tip amount is ',service)
    result = service+amount
    print('You need to pay' , result)    