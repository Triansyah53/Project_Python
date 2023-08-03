import pdb

# sample_files = './python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/programming_language_wikipedia.txt'
# with open(sample_files, 'r') as f:
#     content = f.read()
# print(content)
# pdb.set_trace()

sample_path2 = './python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/list_of_countries_with_no_comma.txt'
with open(sample_path2,'r')as ff:
    # content=ff.read()
    content=ff.readlines()
    list_of_c=[i.strip() for i in content]
    # list_of_c=[]
    # for i in content:
    #     list_of_c.append(i.strip())
print (content)
print(list_of_c)

# pdb.set_trace()