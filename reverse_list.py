# Reversing a list using while loop
def reverse_list(samplelist):
    i = len(samplelist) - 1

    # Iterate till 1st element and keep on decrementing i
    while i >= 0:
        print(samplelist[i])
        i -= 1


samplelist = [12, 35, 9, 56, 24]
print(reverse_list(samplelist))

# Reversing a list using list comprehension
# Syntax of List Comprehension   [expression for item in list]


def invert_list(input_list):
    input_list = [input_list[n] for n in range(len(input_list) - 1, -1, -1)]
    return input_list


input_list = [11, 27, -1, -5, 4, 3]
print(invert_list(input_list))
