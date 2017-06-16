#!/usr/bin/python
# -*- coding: utf-8 -*-

#factorial

def factorial(n):
    a,b = 1,1 
    while(b<=n):
        a=a*b
        b=b+1
    return a

#isprime
def isPrime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return False
    return True