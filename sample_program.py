def call_palindrome_fun(user_str):
    str1 = ""
    for i in user_str:
        str1 = i + str1
    if user_str == str1:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


def call_substring_palindrome(user_str):
    x = []
    for i in range(len(user_str)):
        for j in range(i + 2, len(user_str) + 1):
            x.append(user_str[i:j])
    # return x
    sample_dict = {}
    for i in x:
        sample_dict[i] = call_palindrome_fun(i)
    # return sample_dict
    list = []
    for key in sample_dict.keys():
        if sample_dict[key] == str('Palindrome'):
            list.append(key)
    return list


def call_occurrence_fun(user_str):
    sample_dict = {}
    for i in user_str:
        sample_dict[i] = user_str.count(i)
    return sample_dict


print("Select Option.")
print("1.Palindrome check")
print("2.Substring palindrome check")
print("3.Occurence of each character")
user_opt = int(input("Enter Option: "))
user_str = input("Enter string: ")
if user_opt == 1:
    print(call_palindrome_fun(user_str))
elif user_opt == 2:
    print(call_substring_palindrome(user_str))
elif user_opt == 3:
    print(call_occurrence_fun(user_str))
else:
    print("Pick a valid option")
