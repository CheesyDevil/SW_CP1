#SW 2nd Mapping notes


#What information does map need?
    # a function and a list/tuple
#What does map return?
    #an object
#What is a lambda function
    #A function that only get run where thay are written, 
#How does using a lambda function and the map function shorten your code?
    #It allows yo to write a simple function that you only need to use once in a single line 

nubers=[123,4,567,543,7632,6]
"""numers=[]

for nub in nubers:
    numers.append(nub/2)"""

"""def divide(nuber):
    return nuber/2"""

numers=list(map(lambda nub: nub/2,nubers))


for i, nub in enumerate(nubers):
    print(f"{nub} divided by 2 is {numers[i]}")
