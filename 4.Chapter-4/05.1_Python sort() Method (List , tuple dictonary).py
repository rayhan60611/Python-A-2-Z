''' A function that returns the length of the value with external function:'''

# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)

# print(cars)



''' A function that returns the length of the value without external function:'''
# # def myFunc(e):
# #   return len(e)

# l = [(2, 2, 1), (3, 4, 7), (4, 1, 6), (1, 3 ,9)]

# l.sort(key= lambda e: e[2])

# print(l)


'''Sort a list of dictionaries based on the "year" value of the dictionaries ""with"" external function:'''

# def myFunc(e):
#   return e['year']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)




'''Sort a list of dictionaries based on the "year" value of the dictionaries ""without"" external function:'''
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key= lambda return_value : return_value['year'])   

print(cars)
