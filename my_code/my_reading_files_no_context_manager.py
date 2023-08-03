# demo 1

# import pdb
#
sample_file = './python-selenium-course-material-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/programming_language_wikipedia.txt'
# my_file=open(sample_file,'r')
# content=my_file.read()
# my_file.close()
# my_content_list=content.split('\n\n')
# print(content)
# print(my_content_list)
# print(type(my_content_list))
#
# # pdb.set_trace()


# DEMO2
# my_file=open(sample_file,'r')
# ## content=my_file.readline()
# content=my_file.readlines()
# my_file.close()
# print(content)
# print(type(content))


# gotcha
my_file = open(sample_file, 'r')
content = my_file.read()
print(content)
print('-----')
my_file.seek(0)
content2 = my_file.read()
print(content2)
print('2------')
my_file.close()
