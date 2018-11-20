# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:07:44 2018

@author: Kenya Plenty
"""

from math import sqrt, floor
import random



"""
Finds the GCD of two integers greater than 0 using Euclid's algorithm
"""
def euclidGCD(a,b):
    if a == 0 and b == 0:
        start = str(a)
        end = str(b)
        result = " gcd(" + start + "," + end + ") = N/A"
        return result
    elif a != 0 and b == 0:
        result = "gcd({},{}) = {}".format(a,b,a)
        return result 
    else:
        c = a % b
        print("gcd({},{})".format(a,b))
        print("a:{} b:{} c:{}".format(a,b,c))
        return euclidGCD(b,c)
        
"""
Generates a list of primes using Sieve of Erastosthenes  
"""
def eratosthenesGeneratingPrimes(n):
    result = "List of Primes: "
    if n <= 1: 
        return result 
    else: 
        numbers = {x: True for x in range(2,n+1)}
        primes = []
        for key in numbers:
            if numbers[key]: 
                for i in range(key+1,n+1):
                    if i % key == 0:
                        numbers[i] = False
        for num in numbers.keys():
            if numbers[num]:
                primes.append(num)
        
        return primes
      
"""
Checks if n is prime using trial division
Checks to see if n is divisible by 2 <= i <= square root of n
If it is, then n is composite and the function prints False 
If not, n is prime and the function prints True 

"""
def trialPrimalityCheck(n):
    if n <= 1:
        return "N/A"
    else:
        primes = []
        upperBound = floor(int(sqrt(n))) 
        for i in range(2,upperBound+1):
            possiblePrime = i
            bound = floor(int(sqrt(possiblePrime)))
            primality = True 
            
            for j in range(2,bound+1):
                if possiblePrime % j == 0:
                    primality = False 
                    
            if primality:
                primes.append(possiblePrime)
        
        for p in primes: 
            if n % p == 0:
                result = str(n) + " is composite (not prime) " 
                return result
        
        result = str(n) + " is prime"
        return result 
            
"""
Checks if n is prime using Sieve of Eratosthenes 
"""
def eratosthenesPrimalityCheck(n):
    if n <= 1:
        return "N/A"
    else:
        upperBound = floor(int(sqrt(n)))
        primeList = eratosthenesGeneratingPrimes(upperBound)
        
        for i in range(0,len(primeList)):
            possibleFactor = primeList[i]
            if n % possibleFactor == 0:
                result = str(n) + " is composite (not prime)"
                return result
        
        result = str(n) + " is prime"
        return result 
        

"""
Euclid's Algorithm to find GCD without printing all the steps.
Help for the Fermat method 
"""

def GCD(a,b):
    if a == 0 and b == 0:
        return "N/A"
    elif a != 0 and b == 0:
        return a
    else:
        c = a % b 
        return GCD(b,c)


"""
Checks if n is prime using Fermat Little Theorem
If (a^(n-1) - 1, where 1 < a < n-1) is divisible by n, then n is composite and
the function prints False. 
If (a^(n-1) - 1, where 1 < a < n-1) is not divisible by n, then n is prime
and the function prints True
"""

def fermatPrimalityCheck(n):
    if n <= 1:
        primality = "N/A"
        return primality
    else: 
        done = False 
        while not done:
            a = random.randint(2,n-1)
            if GCD(a,n) == 1:
                done = True 
        
        if a**(n) % n != a:
            primality = str(n) + " is composite (not prime)" 
            return primality 
        else:
            primality = str(n) + " maybe prime" 
            return primality


"""
Generates the prime factorization of n using trial division 
"""
def trialPrimeFactorization(n):
    if n <= 1:
        return "N/A"
    else:
        primes = []
        primeFactors = []
        upperBound = floor(int(sqrt(n))) 
        
        for i in range(2,upperBound+1):
            possiblePrime = i 
            primality = True
            bound = floor(int(sqrt(possiblePrime)))
            for j in range(2,bound+1):
                if possiblePrime % j == 0:
                    primality = False 
            if primality:
                primes.append(possiblePrime)

      while n > 1: 
          for p in primes: 
                
    
            
        
        return primeFactors
            
        
                
                
            
        

                    

"""
Generates the prime factorization of n using Pollard-Strassen
"""
def pollardStrassenPrimeFactorization(n):
    pass 


"""
Generates a list of the first one million primes
"""

def generateMilPrimes():
    milPrimes = []
    with open("primes.txt", "r") as f:
        for line in f:
            primeLine = line.split()
            if len(primeLine) != 0:
                for prime in primeLine:
                    milPrimes.append(prime)
    f.close()
    return milPrimes
    
"""
Calculates the proportion of primes that end with 1, 3, 7, and 9 respectively in the first million primes 
"""
def propLastDigit():
    pl = generateMilPrimes()
    
    propOne = 0.0
    propThree = 0.0
    propSeven = 0.0
    propNine = 0.0
    
    for i in range(0, len(pl)):
        prime = pl[i]
        if prime.endswith("1"):
            propOne += 1
        elif prime.endswith("3"):
            propThree += 1
        elif prime.endswith("7"):
            propSeven += 1
        else:
            if prime.endswith("9"):
                propNine += 1 
      
    
    result = "\n proportion of primes that end with 1: {} \n proportion of primes that end with 3: {} \n proportion of primes that end with 7: {} \n proportion of primes that end with 9: {}". format(propOne/len(pl), propThree/len(pl), propSeven/len(pl), propNine/len(pl))
    return result 
    

"""
Calculates the proportion of primes that end with 1 followed by primes that end in 1, 3, 7, and 9 respectively in the first million primes 
"""
def propOne(): 
    pl = generateMilPrimes()
    
    propOneOne = 0.0 
    propOneThree = 0.0 
    propOneSeven = 0.0 
    propOneNine = 0.0 
    
    for i in range(0,len(pl)-1):
        prime = pl[i]
        foll = pl[i+1]
        if prime.endswith("1"):
            if foll.endswith("1"):
                propOneOne += 1 
            elif foll.endswith("3"):
                propOneThree += 1 
            elif foll.endswith("7"):
                propOneSeven += 1 
            else:
                if foll.endswith("9"):
                    propOneNine += 1 
                    
    result = "\n proportion of primes that end with 1 followed by primes that end in 1, 3, 7, and 9 are respectively: {}, {}, {}, {}".format(propOneOne/len(pl),propOneThree/len(pl),propOneSeven/len(pl),propOneNine/len(pl))
    return result 

"""
Calculates the proportion of primes that end with 3 followed by primes that end in 1, 3, 7, and 9 respectively in the first million primes 
"""    
def propThree():
    pl = generateMilPrimes()
    
    propThreeOne = 0.0 
    propThreeThree = 0.0 
    propThreeSeven = 0.0 
    propThreeNine = 0.0 
    
    for i in range(0, len(pl) - 1):
        prime = pl[i]
        foll = pl[i+1]
        if prime.endswith("3"):
            if foll.endswith("1"):
                propThreeOne += 1 
            elif foll.endswith("3"):
                propThreeThree += 1 
            elif foll.endswith("7"):
                propThreeSeven += 1 
            else:
                if foll.endswith("9"):
                    propThreeNine += 1 
    
    result = "\n proportion of primes that end with 3 followed by primes that end in 1, 3, 7, and 9 are respectively: {}, {}, {}, {}".format(propThreeOne/len(pl),propThreeThree/len(pl),propThreeSeven/len(pl),propThreeNine/len(pl))
    return result 


"""
Calculates the proportion of primes that end with 7 followed by primes that end in 1, 3, 7, and 9 respectively in the first million primes 
"""
def propSeven():
    pl = generateMilPrimes()
    
    propSevenOne = 0.0 
    propSevenThree = 0.0 
    propSevenSeven = 0.0 
    propSevenNine = 0.0 
    
    for i in range(0,len(pl)-1):
        prime = pl[i]
        foll = pl[i+1]
        if prime.endswith("7"):
            if foll.endswith("1"):
                propSevenOne += 1 
            elif foll.endswith("3"):
                propSevenThree += 1 
            elif foll.endswith("7"):
                propSevenSeven += 1 
            else:
                if foll.endswith("9"):
                    propSevenNine += 1 
    
    result = "\n proportion of primes that end with 7 followed by primes that end in 1, 3, 7, and 9 are respectively: {}, {}, {}, {}".format(propSevenOne/len(pl),propSevenThree/len(pl),propSevenSeven/len(pl),propSevenNine/len(pl))
    return result 


"""
Calculates the proportion of primes that end with 9 followed by primes that end in 1, 3, 7, and 9 respectively in the first million primes 
"""
def propNine():
    pl = generateMilPrimes()
    
    propNineOne = 0.0 
    propNineThree = 0.0 
    propNineSeven = 0.0 
    propNineNine = 0.0 
    
    for i in range(0, len(pl)-1):
        prime = pl[i]
        foll = pl[i+1]
        if prime.endswith("9"):
            if foll.endswith("1"):
                propNineOne += 1 
            elif foll.endswith("3"):
                propNineThree += 1 
            elif foll.endswith("7"):
                propNineSeven += 1 
            else:
                if foll.endswith("9"):
                    propNineNine += 1
    
    result = "\n proportion of primes that end with 9 followed by primes that end in 1, 3, 7, and 9 are respectively: {}, {}, {}, {}".format(propNineOne/len(pl),propNineThree/len(pl),propNineSeven/len(pl),propNineNine/len(pl))
    return result 

   
"""
Calculates the number of twin primes in the first million primes 
"""

def calcTwinPrimes():
    p = generateMilPrimes()
    
    numTwinPrimes = 0 
    
    for i in range(0,len(p)):
        prime = int(p[i])
        prev = prime - 2 
        foll = prime + 2 
        if trialPrimalityCheck(foll) or trialPrimalityCheck(prev):
            numTwinPrimes += 1
    
    print(numTwinPrimes)
        

"""
Plots the number of primes that are less than x 
"""
def pi(x):
    numprimes = 0 
    if x < 1:
        return numprimes 
        
     
"""
Visualizes prime numbers in an interesting and cool way 
"""
def visualizingPrimes():
    pass 
            
        
"""
Creates the menu for the functions
"""
def menu():
    menu = {}
    menu["1"] = "Finds GCD of two integers using Euclid's algorithm"
    menu["2"] = "Generates a list of prime numbers using Sieve of Eratosthenes" 
    menu["3"] = "Checks if a number is prime using trial division"
    menu["4"] = "Checks if a number is prime using Sieve of Eratosthenes"
    menu["5"] = "Checks if a number is prime using Fermat Little theorem"
    menu["6"] = "Generates the prime factorization of a number using trial division"
    menu["7"] = "Generates the prime factorization of a number using Pollard-Stressen"
    menu["8"] = "Vizualization of prime numbers"
    
    for option in menu:
        print(option, menu[option])
    print()
        
    selection = input("Input a number indicating the function you would like to use: ")
    print()

    
    if selection == "1":
        a = int(input("Input the first integer: "))
        b = int(input("Input the second integer: "))
        print()
        print(euclidGCD(a,b))
    elif selection == "2":
        num = int(input("Input a number that you would like to generate primes up until: "))
        print()
        l = [str(x) for x in eratosthenesGeneratingPrimes(num)]
        result = "List of Primes: "
        result += ", ".join(l)
        print(result)
    elif selection == "3":
        num = int(input("Input a number to check its primality using trial division: "))
        print()
        print(trialPrimalityCheck(num))
    elif selection == "4":
        num = int(input("Input a number to check its primality using Sieve of Eratosthenes: "))
        print()
        print(eratosthenesPrimalityCheck(num))
    elif selection == "5":
        num = int(input("Input a number to check its primality using Fermat Little Theorem: " ))
        print()
        print(fermatPrimalityCheck(num))
    elif selection == "6":
        num = int(input("Input a number to factor using trial division: "))
        print(trialPrimeFactorization(num))
    elif selection == "7":
        num = int(input("Inpute a number to factor using Pollard-Stressen: "))
        print()
        pollardStrassenPrimeFactorization(num)
    elif selection == "8":
        visualizingPrimes()
    else:
        print("Please input a valid menu option.")
        
        


propLastDigit()
propOne()
propThree()
propSeven()
propNine()
calcTwinPrimes()

        
        
        

    

            
        


        
        

        
        



