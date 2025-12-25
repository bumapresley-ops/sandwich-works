sandwich_orders=['meat sandwitch','fish sandwich','pastrami','tacos']
finished_sandwich=[]
for sandwich in sandwich_orders:
  print("i made your",f"{sandwich.title()}")
  finished_sandwich.append(sandwich)
for sandwich in finished_sandwich:
 print(f"{sandwich.title()}, has been made")

