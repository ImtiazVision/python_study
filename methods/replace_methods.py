# str.replace(old, new, [count]) method replaces all occurrences of old in string with new. Both the old and new parameters are required.

distance_traveled = '5kilometers 8kilometers 9kilometers 54kilometers'

replaced = distance_traveled.replace('kilometers', 'km')
print(replaced)

price = '$100  $200 $300 $400'
replaced_var = price.replace('$', '€')
print(replaced_var)