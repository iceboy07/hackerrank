import math
import os
import random
import re
import sys

def solve(n):
    if (n%2) == 0:
        if n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

if __name__ == '__main__':
    N = int(input())
    solve (N)
