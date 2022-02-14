def findMaximumSum(stockPrice, k):
    # Write your code here
    ## i have to find the stock price of none consecative numbers
    #so i can't have the same number in range of k
    ''' if k = 3 i have to have a different number in 3 consecative months
    it would be best to store the sets of 3 as a array then do a 2d array to add the values to a max variable
    then add an if statment to overwrite the max value if its higher'''
    maxValue = 0
    tempArray = []
    for price in stockPrice:
        if stockPrice[price] not in range(stockPrice[price + k]):
            if ((stockPrice[price:k]) > maxValue):
                tempArray.append((stockPrice[price:k]))

    for x in tempArray:
        for tot in x:
            maxValue += tot
        if maxValue > maxValue:
            maxValue = maxValue
        
