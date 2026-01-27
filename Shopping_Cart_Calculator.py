from collections import defaultdict


class ShoppingCart:
    def __init__(self):
        self.total_items =[]
        self.names=[]
        self.prices=[]
        self.quantities=[]
    def add_item(self,name,price,quantity):
        
        self.names.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)
        #zip(self.names,self.prices,self.quantities)

    def remove_item(self,name):
        x =len(self.names)
        i =0
        
        for i in range(0,x-1):
            if(self.names[i]==name):
                r=i

            self.names.pop(r)
            self.prices.pop(r)
            self.quantities.pop(r)
        else:
            return f"Product : {name} don't exists"
        
    def get_total(self):
        total =[x*y for x,y in zip(self.prices,self.quantities)]
        total_final =sum(total)
        return f"Total coast is {total_final}"
    
    def __len__(self):
        unique = set(self.names)
        t2= len(unique)
        t2 =str(t2)
        return f"No. of unique items are {t2}"
    
    def __str__(self):
    
        return f" Names :{self.names} \n Respective Prices :{self.prices} \n Respective Quantities :{self.quantities}"
    
cart = ShoppingCart()
cart.add_item("Apple",2.5,3)
cart.add_item("Banana",1.2,5)
print(cart)
cart.remove_item("Apple")
print()
print()
print(cart)
print()
print(cart.get_total())
print()
print(cart.__len__())






