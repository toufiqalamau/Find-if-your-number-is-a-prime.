i=int(raw_input('Is your number a prime number? type it here to find out: '))

for x in range(2,10):
    if i%x==0:
        print'it is a composite number.'
        break
    else:
        print 'prime'
        break

        
        
