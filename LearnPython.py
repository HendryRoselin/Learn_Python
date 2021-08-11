import pandas as pd
print("--------------------------------------------")
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
print("--------------------------------------------")
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print("--------------------------------------------")
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print("--------------------------------------------")
print(myvar["y"])
print("--------------------------------------------")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print("--------------------------------------------")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print("--------------------------------------------")
