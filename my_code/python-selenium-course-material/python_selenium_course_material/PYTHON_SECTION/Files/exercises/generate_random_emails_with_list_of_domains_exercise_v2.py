"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V2:
- Create 100 total emails with domains randomly elected from the list. So the number of emails
for each domain will be unknown.
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v2.csv

** the difference from V1 is the domains are random for this one.
"""
import pdb
import random
import string
all_email=[]
output_path="jawaban_v2.csv"
letters=string.ascii_lowercase
list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
for i in range(100):
    domain='@'+random.choice(list_of_domains)
    email=''.join(random.choice(letters)for i in range(10))
    the_email=email+domain
    all_email.append(the_email)
    print(the_email)

with open(output_path,'w')as f:
    f.write('\n'.join(all_email))

# the_answer=[]
# for i in range(100):
#     random_string= ''.join(random.choice(letters)for i in range(10))
#     domain = random.choice(list_of_domains)
#     email=random_string+'@'+domain
#     the_answer.append(email)
# print(the_answer)
#
#
# with open(output_path, 'w') as f:
#     f.write('\n'.join(the_answer))