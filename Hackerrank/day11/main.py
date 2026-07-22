#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    suma_max = -100
    
    for i in range(4):
        for j in range(4):
            sup =  arr[i][j] + arr [i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr [i+2][j] + arr [i+2][j+1] + arr[i+2][j+2]
            suma_actual = sup + mid + bot
            
            if suma_actual > suma_max:
                suma_max = suma_actual
                
print(suma_max)
