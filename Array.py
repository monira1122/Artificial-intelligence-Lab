students=["moni","piya","samiya"]
students[1]="salman"
print(students)

#Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW","toyota"]

x=len(cars)

print(x)

#Print each item in the cars array:
cars = ["Ford", "Volvo", "BMW"]

for i in cars:
  print(i)
  #Add one more element to the cars array:
  cars=["volvo","toyota","BMW"]
  cars.append("Ford")
  print(cars)
#Delete the second element of the cars array:
cars=["volvo","toyota","BMW"]
cars.pop(0)
print(cars)
#Delete the element that has the value "Volvo":

cars=["volvo","toyota","BMW"]
cars.remove("volvo")
print(cars)

#count
fruits=["Apple","Banana","Mango","Mango"]
x=fruits.count("Mango")
print(x)

#sort
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

#insert
students=["moni","piya","samiya","salman"]
students.insert(1,"santo")
print(students)