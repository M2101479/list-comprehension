numbers = [i for i in range(1001)]
print(numbers)


numbers2 = [i for i in range(1001) if i % 8 == 0]
print(numbers2)

numbers3= [i for i in range(1001) if "6" in str(i) ]
print(numbers3)

string = "Practice Problems to Drill List Comprehension in Your Head."

check = len([i for i in string if i == " "])
print(check)
  
remove ="".join([i for i in string if i not in ["a","e","i","o","u"]]);
print(remove)

words=string.split("  ")
five= [i for i in string if len(words) < 5]

numbers6 = [num for num in range(1, 1001) if any(num % div == 0 for div in range(2, 10))]
print(numbers6)



#Find all of the words in a string that are less than 5 letters (use string above)
#Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
