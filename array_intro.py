foods = ["Apple", "Orange", "Grapes", "Mango", "Banana"] # 5x5 = 25 bytes of storage

print(foods[3]) # O(1)

foods.pop() # O(1)
print(foods)

foods.append("Pineapple") # O(1)
print(foods)

foods.insert(2, "Peach") # O(n)
print(foods)

foods.pop(0) # O(n)
print(foods)

foods.remove("Peach")
print(foods)

del foods[2:3]
print(foods)


def func(mylist):

    for i in range(0,len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i] 
    return 0


print(func([1,9,8,5,2,8,2,6]))