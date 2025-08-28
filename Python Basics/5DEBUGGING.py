# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.debug('Start of program')

# def factorial(n):
#     logging.debug('Start of factorial(' + str(n) + ')')
#     total = 1
#     for i in range(n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(' + str(n) + ')')
#     return total

# print(factorial(5))
# logging.debug('End of program')

# 2035-05-23 16:20:12,664 - DEBUG - Start of program
# 2035-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
# 2035-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
# 2035-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
# 2035-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
# 2035-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
# 2035-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
# 2035-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
# 2035-05-23 16:20:12,680 - DEBUG - End of factorial(5)
# 0
# 2035-05-23 16:20:12,684 - DEBUG - End of program


# Practice Questions
#   1.  Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
# spam = input()
# assert int(spam) < 10

#   2.  Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other,
# even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
# eggs = input(); bacon = input()
# assert eggs != bacon

#   3.  Write an assert statement that always triggers an AssertionError.
# assert False

#   4.  What two lines must your program have to be able to call logging.debug()?
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

#   5.  What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?
# import logging
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

#   6.  What are the five logging levels?

#   7.  What line of code can you add to disable all logging messages in your program?

#   8.  Why is using logging messages better than using print() to display the same message?

#   9.  What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# 10.  After you click Continue, when will the debugger stop?

# 11.  What is a breakpoint?

# 12.  How do you set a breakpoint on a line of code in Mu?

# Practice Program: Debugging Coin Toss
# The following program is meant to be a simple coin toss guessing game. The player gets two guesses. (It’s an easy game.)
# However, the program has multiple bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug("Guess is gotten")
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

toss = "tails" if toss == 0 else "heads"


if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')