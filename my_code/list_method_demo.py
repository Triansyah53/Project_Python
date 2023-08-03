countries=["indonesia",'canada','india','japan','usa']
print(type(countries))
numberofelemen=print(len(countries))

countries.append('china')
print(countries)

countries.remove('canada')
print(countries)

check= countries.pop()
print(countries)
print(check)
