
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = meal_cost *(tip_percent/100)
    tax_percent = meal_cost *(tax_percent/100)
    totalCost =int( meal_cost + tip_percent + tax_percent)
    print(totalCost)



if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
