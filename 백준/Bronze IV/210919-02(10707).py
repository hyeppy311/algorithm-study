x_price = int(input())
y_price = int(input())
y_limit = int(input())
y_plus = int(input())
j_water = int(input())

X = x_price * j_water

if j_water <= y_limit :
  print(y_price)

elif j_water > y_limit :
  add_price = (j_water - y_limit)*y_plus
  print(y_price+add_price)

X = x_price * j_water

