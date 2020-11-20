def raindrops(n):       #defined a function raindrops
    b = ''              
    if (str(n).isnumeric()==False):     #Check if input is string
        return ("Error!! Please enter a number")    
    if (n==0):          #if the number is zero it would be assigned to the variable
        b=str(n)
    else:
        if (n%3==0):    #if the number is divisible by 3 Pling would be added to the variable
            b=b+'Pling'
        if (n%5==0):    #if the number is divisible by 5 Plang would be added to the variable
            b=b+'Plang'
        if (n%7==0):    #if the number is divisible by 7 Plong would be added to the variable
            b=b+'Plong'
        if (b==''):     #if the variabe is null till this point the number would be assigned to the variable
            b=str(n)
    return b