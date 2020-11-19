import re
sample_str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', sample_str)
# If-statement after search() tests if it succeeded
if match:
    # 'found word:cat'
    print('found', match.group())
else:
    print('did not find')
# found, match.group() == "iii"
match = re.search(r'iii', 'piiig')
print(match.group())
# not found, match == None
# match = re.search(r'igs', 'piiig')
# print(match.group())
# . = any char but \n
# found, match.group() == "iig"
match = re.search(r'..g', 'piiig')
print(match.group())
# \d = digit char, \w = word char
# found, match.group() == "123"
match = re.search(r'\d\d\d', 'p123g')
print(match.group())
# found, match.group() == "abc"
match = re.search(r'\w\w\w', '@@abcd!!')
print(match.group())
# To find if it is a email
sample_str1 = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', sample_str1)
if match:
    # 'b@google'
    print(match.group())
