from itertools import product
from pickle import LIST


class User:
   def __init__(self, id:int, user_name:str, balance:float):
        self.id=id
        self.user_name=user_name
        self.balance=balance
        self.order_list = []
        self.carrito_list=[]

   def add_product_to_car(self,product):
    if product in self.carrito_list:
     return "Producto ya agregado"
    else:
     self.carrito_list.append(product)
     product.product_list.append(self)
    return "Producto obtenido con exito"
  
   def cancelar_producto_agregado(self,product):
    if product in self.carrito_list:
      self.carrito_list.remove(self)
      return "cancelacion exitosa"
    else:
      return "No tiene producto en carrito"

   def consolidate_order(self):
      for i in range(0,-1):
        print(i)
        carrito_list.sort()
        print("orden",carrito_list)
    
   def add_to_balance(self,amount=float):
    if amount in carrito_list:
      return "balance agregado"
    else:
     self.carrito_list.append(amount)
     amount.product_list.append(self)
    return "balance obtenido con exito"

   def plot_order_history(self):
    return [i.id for i in self.carrito_list]



class order:
  def __init__(self,id=int,date=date,total=float,status=bool):
    self.id=id
    self.product_list=[]
    self.date=date
    self.total=total
    self.status=status
  
  

class product:
  def __init__(self,id=int, name=str, price=float):
    self.id=id
    self.name=name
    self.price=price
    self.price_history={price}
  
  def update_price(self,new_price=float):
    dict.update(new_price)
    print(dict)
