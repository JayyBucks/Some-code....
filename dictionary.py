# dictionary_list = [
#     {"name": "Carl",
#      "Tall": False,
#      "age": 17,
#      "fit": True},
#     {"name": "Josh",
#      "Tall": True,
#      "age": 16,
#      "fit": True}
# ]
# for dictionary in dictionary_list:
#     print(dictionary["name"])

Lamborghini = [
    {"Make": "Lamborghini",
     "Model": "Aventador",
     "Year": "2017",
     "Value": 640000,
     "Engine": 6.5},
     {"Make": "Lamborghini",
     "Model": "Veneno",
     "Year": "2013",
     "Value": 4000000,
     "Engine": 6.5}
    
]
Ford = [{"Make": "Ford",
     "Model": "GT",
     "Year": "2017",
     "Value": 500000,
     "Engine": 3.5}
]

car_dictionary = { "Lamborghini": Lamborghini, "Ford": Ford}
for marke, car in car_dictionary.items():
    for feature, value in car.items():
        print(f" {feature}: {value}")

#print all lambo info
#print all ford info

