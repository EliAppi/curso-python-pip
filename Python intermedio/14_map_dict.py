items=[
  {
    "producto":"camisa",
    "price":20,
  },
  {
    "producto":"pantalon",
    "price":80
  },
  {
    "producto":"tenis",
    "price":100
  },
]

prices=list(map(lambda item: item["price"], items)) #agrego nuevo item (prices)
print(prices)

def add_taxes(item):
  item["taxes"]=item["price"]*.19 #creo una funcion para clcular impuestos
  return item

new_items=list(map(add_taxes, items)) #agrego nuevo item imouestos(taxes)
print(new_items)