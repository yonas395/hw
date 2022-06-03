
import math
from random import randint


 1.Compute the sum of digits in all numbers from 1 to n
# O(n)
 random_number = int(input('enter any random number: '))

 result = 0

 for i in range(1, random_number + 1):
    result = result + i

 print(result)






# ------Q 2.Find max number-------#

#O(n)
 list = [126, 465, 789]

big_num = list[0]
 for i in range(0, len(list), 1):
    big_num = max(big_num, list[i])

 print(big_num)




#------- Q3 Count odd and even numbers ---#
# Count odd and even digits of the whole number.
#O(n)
list1 = [1, 5, 9, 2, 6, 8, 4, 7, 5, 3]
total_even = 0
total_odd = 0

for number in list1:
    if(number % 2 == 0):
        total_even = total_even + 1
    else:
        total_odd = total_odd + 1

print('total even:=', total_even)
print('total odd:=', total_odd)
