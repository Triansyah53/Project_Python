# example of using keyword parameter
# example one : write a function that will return a words that have X length, given a string

# def getcount(input_string, max_size=3):
#     small_words = []
#     for word in input_string.split():
#         if len(word) <= max_size:
#             small_words.append(word)
#     return len(small_words), small_words
#
#
# inputed = "We already have one file under the functions folder for an example."
# balik = getcount(inputed,max_size=5)
#
# print(balik)

# make a function that
# print the length of list
# the list contain all of the word that have less than 4 character

# def list_length(inputed_words,max_size=4):
#     the_list=[]
#     for word in inputed_words.split():
#         if len(word) < max_size:
#            the_list.append(word)
#     return the_list
#
# inputed=('We already have one file under the functions folder for an example')
# check=list_length(inputed)
# print(len(check))

# def list_length(inputed_word, max_size=3):
#     container=[]
#     for word in inputed_word.split():
#         if len(word)<=max_size:
#             container.append(word)
#     return  len(container),container
#
# inputhere = ('We already have one file under the functions folder for an example')
# check=list_length(inputhere)
# print(check)


# EXAMPLE 2
def connect_to_database(host='test.db.com', username='testuser', password='tesspassword'):
    print(f"connection to host: {host}")
    print((f"username is : {username}"))


connect_to_database()