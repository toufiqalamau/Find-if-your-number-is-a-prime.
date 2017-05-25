i=int(raw_input('Is your number a prime number? type it here to find out. exclude 2: '))

for x in range(2,10):
    if i%x==0:
        if i==2:
            print 'prime.'
            break
        print'it is a composite number.'
        break
        
    else:
        print 'prime'
        break
    

#this program has a major flaw...when the input is from 1-10, it will give 'composite'
#result even for the prime numbers.
