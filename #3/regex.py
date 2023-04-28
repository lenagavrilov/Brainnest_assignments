import re
"""
1. Write a regular expression that matches a date in the format dd/mm/yyyy.
For example, the string \"01/01/2021\" should match."
"""
date_reg = re.compile(r'\d{2}/\d{2}/\d{4}')
print('date_reg: ', date_reg.findall('Today is 24/04/2023 and not 23/5/2023'))

"""
2. Write a regular expression that matches a phone number in the format xxx-xxx-xxxx, where x is a digit. 
For example, the string \"123-456-7890\" should match."
"""
phone_reg = re.compile(r'\d{3}-\d{3}-\d{4}')
print('phone_reg: ', phone_reg.findall('The right phone number is 123-456-7890'))

"""
3. Write a regular expression that matches a valid email address. 
For example, the string \"example@example.com\" should match."
"""
#email_reg = re.compile(r'\w+@[a-zA-Z]+/.\[a-zA-Z]{2,3')
email_reg = re.compile(r'[a-zA-Z0-9-_]+@{1}[a-zA-Z-]+\.[a-zA-Z]{2,3}')
print('email_reg: ', email_reg.findall('The mails are new_example@google.com, e-xample_22@google.de'))

"""
4. Write a regular expression that matches a string that starts with a word, followed by one or more whitespace characters, 
followed by another word. For example, the string \"hello world\" should match."
"""
string_reg = re.compile(r'\b\w+\s+\w+')
print('string_reg: ', string_reg.findall('hello world'))

"""
5. Write a regular expression that matches a string that contains a number with exactly two decimal places. 
For example, the string \"1.23\" should match, but the string \"1.234\" should not match."
"""
decimal_reg = re.compile(r'\d+\.\d{2}\b')
print('decimal_reg: ', decimal_reg.findall('This is correct: 1.23 but this is not: 1.234'))

