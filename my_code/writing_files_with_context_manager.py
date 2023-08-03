##ex1
# my_string="i love to program in python"
# with open('./python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/sample_output2.txt','w') as f:
#     f.write(my_string)


#ex 2
# my_list=['user1','user2','user3']
#
# with open('./python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/sample_output2.txt','w')as f:
#     for i in my_list:
#         # f.write(i+'\n')
#         f.write(i + '\t')

#ex3
# var2='i also love testing'
# with open('./python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/sample_output.txt','a') as f:
#     f.write('\n'+var2)

#ex4
my_lang=['python','java','golang','javascript','flutter']
with open('./python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/csvexample.csv','w')as f:
    # for i in my_lang:
        tes= '\n'.join(my_lang)
        f.write(tes)
        # f.write(i+'\n')
