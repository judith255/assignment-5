#list of available cars and their prices
cars={
"Toyata Corolla" :50000,
"Ford":80000, 
"lexus":100000,
"G-Wagon":200000,
"ferrari" :50000,
"SUV":30000, 
"Porsche":50000,
"Lamborghini":80000,
 }
#get user input for car name 
car_name=input("Enter a car_name:")
#check if car name is in the available cars 
if car_name in cars:
  print("Yes")
  #if car name is present ,get its price
  car_price=cars[car_name]
  print(f"The price of {car_name}is ${car_price}.")
else:
  #if car name is not present,inform the user
  print(F"Sorry,{car_name}is not available. ")
#the link for my Github respository
#https://github.com/judith255/assignment-5