def create_list(limit, step):
    #i = 0
    numbers = []
    
    #while i < limit:
    #    print "At the top i is %d" % i
    #    numbers.append(i)
        
    #    i = i+step
    #    print "Numbers now: ", numbers
    #    print "At the bottom i is %d" % i
	 
    for i in range(0, limit, step):
        numbers.append(i)	
    return numbers
	
print "The numbers: "
numbers = create_list(6, 2)
for num in numbers:
    print num