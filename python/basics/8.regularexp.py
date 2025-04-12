import re

phone_number_regex =  re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phone_number_regex.search("My numbger is 100-389-4888 100-389-4883")
print(mo.group())

# grouping with parentiesis
phone_number_regex =  re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_number_regex.search("My numbger is 100-389-4888 100-389-4883")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())


# Just covered the basics but need to write a proper doc