"""
We will generate a random interger between 1-20.
Based on results of random number, we check to see if it falls under certain range.
If num > 15 = "Cherries"
If num > 10 = "Orange"
If num > 5 = "Plum"
If num > 2 = "Melon"
If num > 1 = "Bell"
If num not above any = "Bar"

We iterate over using a loop 3 times and print results to the user. 
For example "Plum Charries"
"""
"""
import random
num = generate random number

If num > 15
result = "Cherries"
If num > 10
result = "Orange"
If num > 5
result = "Plum"
If num > 2
result = "Melon"
If num > 1
result = "Bell"
else
result = "Bar"

loop 3 times
print output (fruit) to user
"""
import random
def main():
    for i in range(0, 3):
        spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if (rand_num > 15):
        output = "Cherries"
    elif (rand_num > 10):
        output = "Orange"
    elif (rand_num > 5):
        output = "Plum"
    elif (rand_num > 2):
        output = "Melon"
    elif (rand_num > 1):
        output = "Bell"
    else:
        output = "Bar"
    print(output, end=" ")

main()