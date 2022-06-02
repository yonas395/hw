# 1.split in half

# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.

# string slicing
# O(2)

test_str = "codingisfun"

print("The original string is : " + test_str)

first_half, second_half = test_str[:len(test_str)//2], test_str[len(test_str)//2:]


print("The first part of string : " + first_half)
print("The second part of string : " + second_half)

##-------------Unique Characters in String------------###
# Approach 1 – Brute Force technique: Run 2 loops with variable i and j. Compare str[i] and str[j].
# If they become equal at any point, return false.

# O(n2)
str = input("pleas put word: ")

def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if(str[i] == str[j]):
                return False

    return True




if(uniqueCharacters(str)):
    print("The String ", str," has all unique characters");
else:
    print("The String ", str, " has duplicate characters");
