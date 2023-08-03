liist = ['samsung','apple', 'nokia', 'nothing']
print(liist)
liist.append('xiaomi')
print(liist)
x=liist.pop(1)
print(liist)

index_of= liist.index('xiaomi')
print(index_of)

liist.insert(2,'apple')
print(liist)

liist[2]='replace'
print(liist)

liist.remove('replace')
print(liist)