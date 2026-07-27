#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    S = input("Introduce el texto o numeros que desees: ").strip
    try:
        print(int(S))
    except ValueError:
        print("Bad String")