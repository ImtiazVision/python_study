# We use '==' to compare the contents inside of 2 lists. 
# We use 'is' to compare the identity of 2 lists. 

print([1,3] == [1,3]) # True
print([1,3] == [1,3,9]) # False
print([1,3] == [3,1]) # False