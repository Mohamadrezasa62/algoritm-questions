t = int(input())
my_string = 'codecup6'

# method 1 that isn't so good
# number = t // len(my_string)
# my_string += number * my_string
# print(my_string[t-1])

# method 2
number = t % len(my_string)
print(my_string[number - 1])
