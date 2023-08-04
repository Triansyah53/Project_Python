"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""
# Obtain the list of emails using get_emails_from_file.
# Count the domains and store the counts using count_domains_option_1.
# Save the domain counts to a JSON file using save_output_in_json_file.
# Print the domain counts dictionary.

input_file = "count_domains_in_email_list_file_exercise_input.csv"
output_file = "count_domains_in_email_list_file_exercise_output.json"

def get_emails_from_file(file_path):
    with open(file_path,'r')as f:
        raw=f.readlines()
        clean=[i.strip(',\n') for i in raw]
        return clean

def count_domain_ops1(file_path):
    email_counts=dict()
    for email in email_list:
        domain=email.split('@')[-1]
        if domain not in email_counts.keys():
            email_counts[domain]=1
        else:
            email_counts[domain]=email_counts[domain]+1
    return email_counts

email_list=get_emails_from_file(input_file)

counts1=count_domain_ops1(email_list)
print(counts1)
