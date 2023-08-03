# capitals ={"USA":"washington dc", "france":'paris', "indonesia":"jakarta"}
# print(type(capitals))
# capitals["malaysia"]="kuala lumpur"
# print(capitals)
#
# capitals.update({"australia":"canberra"})
# print(capitals)
#
# capitals.update({"indonesia":"bali"})
# print(capitals)

capitals = {"USA": "washington dc", "france": 'paris', "indonesia": "jakarta"}
allkey = capitals.keys()
allvalues = capitals.values()
tes = f"{allkey}{allvalues}"
print(tes)
print("this is {}, this is {}".format(allkey, allvalues))
