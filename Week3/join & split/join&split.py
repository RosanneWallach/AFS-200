csv = "Eric,John,Michael,Terry,Graham,TerryG,Brian"

friends_list = []

a = csv.split(',')
print(a)

for x in a :
  friends_list.append(x)

print(friends_list)

for x in friends_list :
  print(x)