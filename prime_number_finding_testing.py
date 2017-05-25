inpt=int(raw_input('Except 1,2,3,5,7 known primes, type a big number to see the list of primes upto your number: '))

l=range(inpt)
l.remove(0)
prime=[]
prml=[1,2,3,5,7]

  

for i in prml:
    prime.append(i)


for i in l:
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                if i%7!=0:
                    prime.append(i)
                
prime.remove(1)
prime.sort()
print 'if you want to see your list, then type \'prime\' in the promt.'   
