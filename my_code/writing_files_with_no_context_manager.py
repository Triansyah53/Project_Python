my_string ="i love to program in python"

#example 1

my_file=open('./python-selenium-course-material/python_selenium_course_material/PYTHON_SECTION/Files/sample_files/sample_output.txt', 'w')
my_file.write(my_string+ ('\n'))
my_file.write(my_string)
my_file.write('\n')
my_file.write(my_string)
my_file.close()