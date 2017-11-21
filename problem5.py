# Smallest multiple
'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

import math

divisorMax = 20
top = divisorMax + 1

p = [x for x in range(2,top)]
for num in p:
  for idx in range(2,(top//num)+1):
    if num*idx in p:
      p.remove(num*idx)

result = 1

for i in range(0, len(p)):
    a = math.floor(math.log(divisorMax) / math.log(p[i]))
    result = result * (p[i]**a)

print(result)