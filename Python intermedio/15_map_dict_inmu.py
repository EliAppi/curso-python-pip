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

prices=list(map(lambda item: item["price"], items)) #listo unicamente (prices)
print(prices)

def add_taxes(item):
  new_item=item.copy() #creo una copia del dict original para que no se modifique
  new_item["taxes"]=new_item["price"]*.19 #creo una funcion para clcular impuestos
  return new_item

new_items=list(map(add_taxes, items)) #agrego nuevo item impuestos(taxes)
print(items)
print(new_items)