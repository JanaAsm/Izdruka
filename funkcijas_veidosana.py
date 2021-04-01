

#go to restaurant
def eat():
    #everything after indent will be run by this function
    print("Hello")
    print("Let's order some food")
    print("Lets eat")
    print("Let's leave and be happy")
#call the function 2 times
eat()
eat()
#we can give our functions parametrs and those parameters take arguments
def order_food(dish):
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")

order_food("potatoes")
order_food("ice cream")

#String to be splitted
St = 'where is my violet flower'

#Split the string on blank characters
List = St.split()

#for each element in the list, if it starts with 'm' then print it
for s in List:
    if s.startswith('v'):
        print(s)