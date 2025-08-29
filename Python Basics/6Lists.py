# import random, sys, time

# WIDTH = 70  # The number of columns

# try:
#     # For each column, when the counter is 0, no stream is shown.
#     # Otherwise, it acts as a counter for how many times a 1 or 0
#     # should be displayed in that column.
#     columns = [0] * WIDTH
#     while True:
#         # Loop over each column:
#         for i in range(WIDTH):
#             if random.random() < 0.02:
#                 # Restart a stream counter on this column.
#                 # The stream length is between 4 and 14 characters long.
#                 columns[i] = random.randint(4, 14)

#             # Print a character in this column:
#             if columns[i] == 0:
#                 # Change this ' '' to '.' to see the empty spaces:
#                 print(' ', end='')
#             else:
#                 # Print a 0 or 1:
#                 print(random.choice([0, 1]), end='')
#                 columns[i] -= 1  # Decrement the counter for this column.
#         print()  # Print a newline at the end of the row of columns.
#         time.sleep(0.1)  # Each row pauses for one tenth of a second.
# except KeyboardInterrupt:
#     sys.exit()  # When Ctrl-C is pressed, end the program.


# Practice Questions
#   1.  What is []? None list

#   2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# spam = [2, 4, 6, 8, 10]
# spam[2] = "hello"
# print(spam[2])

# For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

#   3.  What does spam[int(int('3' * 2) // 11)] evaluate to? spam[3]

#   4.  What does spam[-1] evaluate to?

#   5.  What does spam[:2] evaluate to?

# For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].
# bacon = [3.14, "cat", 11, "cat", True]

# #   6.  What does bacon.index('cat') evaluate to?
# bacon.index('cat')

# #   7.  What does bacon.append(99) make the list value in bacon look like?
# bacon.append(99)
# print(bacon)

# #   8.  What does bacon.remove('cat') make the list value in bacon look like?
# bacon.remove('cat')
# print(bacon)

#   9.  What are the operators for list concatenation and list replication?
bacon = [3.14, "cat", 11, "cat", True]
cat = ['a', 'b', 'c', 'd']
concat = bacon + cat
print(concat)
copy1 = concat.copy()

# 10.  What is the difference between the append() and insert() list methods?

# 11.  What are two ways to remove values from a list?
copy1.remove('a')
copy1[0] = None
print(copy1)

# 12.  Name a few ways that list values are similar to string values.


# 13.  What is the difference between lists and tuples? tuple = ('k', 'a', 'l') not rewritable

# 14.  How do you write the tuple value that has just the integer value 42 in it?
tuple = (42)
print(tuple)

# 15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?

# 16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

# 17.  What is the difference between copy.copy() and copy.deepcopy()?

# Practice Programs
# For practice, write programs to do the following tasks.
print('-' * 300)
# Comma Code
# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
# with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
    wcommas = ""
    for i in range(0, len(list) - 1):
        wcommas = wcommas + list[i] + ", "
    wcommas = wcommas + "and " + list[-1]
    return wcommas
    

print(comma(spam))

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(lst):
    return ", ".join(lst[:-1]) + " and " + lst[-1]

print(comma(spam))


print('-' * 300)

# Coin Flip Streaks
# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an H for each heads and a T for each tails, 
# you’ll create a list that looks like T T T T H H H H T T. If you ask a human to make up 100 random coin flips, you’ll probably end up 
# with alternating heads-tails results like H T H T H H T H T T—which looks random (to humans), but isn’t mathematically random. 
# A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. 
# Humans are predictably bad at being random.

# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. 
# Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, 
# and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times 
# so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. 
# As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

# import random

# list = []
# contains = 0

# for i in range (0, 100_000):
#     for i in range(0, 100):
#         list.append(random.choice(('T', 'H')))
#     doesContain = False
#     for i in range(0, 100 - 5):
#         if list[i] == list[i + 1] == list[i + 2] == list[i + 3] == list[i + 4] == list[i + 5]:
#             doesContain = True
#     list = []
#     if doesContain: contains += 1 

# print(str(contains / 100000 * 100) + " %")


# Вот подборка задач разного уровня по теме **списки** (как в твоём уроке):

# ---

# ### Базовые

# 1. Создай список из 5 любых животных. Выведи:

#    * первый элемент,
#    * последний элемент (через отрицательный индекс),
#    * срез из первых трёх элементов.

# 2. Пусть есть список чисел `[2, 4, 6, 8, 10]`.
#    Замени третий элемент на `'hello'` и выведи результат.

# 3. Дан список `['cat', 'dog', 'bat']`. Добавь в него `'moose'` через `append()` и `'chicken'` на позицию 1 через `insert()`.

# 4. Удали из списка `['a', 'b', 'c', 'd']` элемент с индексом 2 с помощью `del`, а потом `'b'` с помощью `remove()`.

# ---

# ### Средние

# 5. Напиши программу, которая спрашивает у пользователя имена животных, складывает их в список, а в конце выводит:

#    ```
#    У меня есть: кот, собака, мышь и попугай
#    ```

#    (Подсказка: формат похож на задачу *Comma Code*).

# 6. Создай список чисел от 1 до 20.

#    * Выведи только чётные,
#    * переверни список (`reverse()`),
#    * отсортируй в обратном порядке (`sort(reverse=True)`).
list = [i for i in range(1, 21)]
even = []
for i in range(20):
    if list[i] % 2 == 0:
        even.append(list[i])

print(even)
even.sort(reverse=True)
print(even)

# 7. Есть список `['a', 'b', 'c', 'd', 'e']`. С помощью цикла `for` и `enumerate()` выведи:
list = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list):
    print("Index " + str(i[0]) + " -> " + i[1])

#    ```
#    Index 0 -> a
#    Index 1 -> b
#    ...
#    ```

# ---

# ### Продвинутые

# 8. Напиши функцию, которая принимает список и возвращает новый список без дубликатов (например, `[1, 2, 2, 3]` → `[1, 2, 3]`).
list = [1, 2, 2, 22, 2, 3, 3, 4, 3]
#       0  1  2  3   4  5
toDelete = []

list.sort()

for i in range(1, len(list)):
    if list[i - 1] == list[i]:
        toDelete.append(list[i])
for i in range(0, len(toDelete)):
    list.remove(toDelete[i])

print(list)

# 9. Сгенерируй список из 20 случайных чисел от 1 до 10. Посчитай, сколько раз встречается каждое число.

# 10. Напиши программу, которая генерирует список из 100 подбрасываний монетки (`'H'` или `'T'`) и проверяет, есть ли там серия из 6 одинаковых подряд.

# ---

# Хочешь, я составлю **тест с вариантами ответа** (по типу вопросов в конце главы) или лучше оставить только задачи на код?
