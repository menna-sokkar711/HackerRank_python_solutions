import re
import email.utils
pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

n = int(input())

for _ in range(n):
    parsed = email.utils.parseaddr(input())
    email_address = parsed[1]
    
    if re.match(pattern, email_address):
        print(email.utils.formataddr(parsed))