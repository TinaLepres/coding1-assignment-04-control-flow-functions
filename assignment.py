def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: I got as an answer 3, and 4
# The loop goes through the numbers 1, 2, and 3 in order. 
# The if condition checks whether each number is greater than 1. 
# Since 1 does not satisfy the condition, it is skipped. 
# The numbers 2 and 3 satisfy the condition, so they are passed to add_one, 
# which adds 1 to each number. The results, 3 and 4 sooo.
#
#
# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add_one(2) returns 3 because the function adds 1 to the given number.
# The return statement gives the result back to the code that called the function,
# while print displays the result on the screen. Here, the function calculates
# the result, and print makes it visible in the output.
