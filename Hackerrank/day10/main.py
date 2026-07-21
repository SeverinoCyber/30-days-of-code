#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binario = bin(n)[2:]

    grupos_de_unos = binario.split('0')

    max_unos = max(len(grupo) for grupo in grupos_de_unos)

    print(max_unos)