
def findMaximumSum(stockPrice, k):
    # Write your code here
    ## i have to find the stock price of none consecative numbers
    #so i can't have the same number in range of k
    ''' if k = 3 i have to have a different number in 3 consecative months
    it would be best to store the sets of 3 as a array then do a 2d array to add the values to a max variable
    then add an if statment to overwrite the max value if its higher'''

    
    maxValue = 0 # stores the value of the sum
    tempArray = [] # stores all ints in the compatible range
    for price in stockPrice:
        print(price) #manually running through every element
        if price not in (stockPrice[price + k]): # will scan the next amount of elements to see if there is a similar num
                tempArray.append((stockPrice[price:(price + k)]))# this will append the next sub array to our temparray

    print(tempArray)# check to see if the 2d array was formed
    
    # this will check the 2d array for the max value
    for x in tempArray:
        for tot in x:
            maxValue += tot
        if maxValue > maxValue:
            maxValue = maxValue
    return maxValue 

values = [1,2,3,45]         
findMaximumSum[values, 2]