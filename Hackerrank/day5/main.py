#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(10):
        i += 1
        print(f"{n} x {i} = {n * i}")
