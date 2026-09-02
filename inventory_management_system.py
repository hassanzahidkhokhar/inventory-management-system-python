class Product:
    def __init__(self,prod_id,name,price,quantity):
        self.prod_id = prod_id
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def add_stock(self,stock):
        total = stock + self.__quantity
        self.__quantity = total
        print("After adding your total is ",total)

    def remove_stock(self,stock):

        if stock > self.__quantity:
            print("Reject",
                  self.__quantity)
        elif stock <= self.__quantity:
            new_total = self.__quantity - stock
            self.__quantity = new_total
            print("After mius your total is ",new_total)

    def show_info(self):
        print("Your product id is ",self.prod_id)
        print("Your product name is ",self.name)
        print("Your product price is ",self.__price)
        print("Your product quantity is ",self.__quantity)

    def get_price(self):
        return self.__price

    def set_price(self,new_price):
        self.__price = new_price

    def get_quantity(self):
        return self.__quantity
    
    def product_type(self):
        pass


class Electronics(Product):
    def __init__(self, prod_id, name, price, quantity,warranty):
        self.warranty = warranty
        super().__init__(prod_id, name, price, quantity)

    def product_type(self):
        print("Electronics class")

    def show_info(self):
        super().show_info()
        print("Your product warranty time is ",self.warranty)

class Clothing(Product):
    def __init__(self, prod_id, name, price, quantity,size,brand):
        self.size = size 
        self.brand = brand
        super().__init__(prod_id, name, price, quantity)

    def product_type(self):
        print("Clothing")

    def show_info(self):
        super().show_info()
        print("Your product size is " ,self.size)
        print("Your product brand is ",self.brand)





p1 = Product(5598,"Harpic",1000,10)
p1.add_stock(15)
p1.remove_stock(10)
p1.show_info()
print(p1.get_price())
p1.set_price(1200)
print("After using setting method your new price is",p1.get_price())
p1.get_quantity()
p1.product_type()

e1 = Electronics(4433,"juicer machine",3000,1,20)
e1.product_type()
e1.show_info()

c1 = Clothing(1122,"Shirt",1500,1,"medium","outfitters")
c1.product_type()
c1.show_info()