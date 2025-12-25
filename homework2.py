sandwich_orders=['pastrami','meat sandwitch','fish sandwich','pastrami','tacos','pastrami']
finished_sandwich=[]
print("we no longer have pastrami in the deli!!")
while "pastrami" in sandwich_orders:
 sandwich_orders.remove("pastrami")
 for sandwich in sandwich_orders:
  finished_sandwich.append(sandwich)
  print(finished_sandwich)                                                                                                                                                          ' '