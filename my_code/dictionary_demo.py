
# # getting item form dictionaries
# france_capital = capitals["france"]
# countries = capitals["france"]
# print(france_capital)
# print(countries)
#
# get_value =capitals.get("france")
# print(get_value)
#
# #get key that doesnot exist
#
# getvalued = capitals.get("jakarta")
# print(getvalued)
#
# #return default value if key doesnt exist
# getvalued = capitals.get("jakarta",'no value')
# print(getvalued)

#adding item to dictionary
capitals ={"USA":"washington dc", "france":'paris', "indonesia":"jakarta"}
print(type(capitals))
capitals["malaysia"]="kuala lumpur"
print(capitals)

capitals.update({"australia":"canberra"})
print(capitals)

capitals.update({"indonesia":"bali"})
print(capitals)


employee={"name":"Adit",
          "age":25,
          "phone":6281290038192,
          "Title":"senior software engineer",
          "skills":["AWS","Python","SQL"]}
print(employee["name"])
print(type(employee["skills"]))
tess=len(employee["skills"])
print(tess)
print(f"user has {tess} skills")
