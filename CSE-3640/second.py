class CustomerOrder:
    def __init__(self):
        self.orders=[]
    
    def add_order(self,orderid,cusname,orderamount):
        order={"id":orderid, "customer name":cusname,"order amount":orderamount}
        self.orders.append(order)

    def print(self):
        print("Customer Details:")
        for order in self.orders:
            print(f"Customer ID:{order['id']} Customer Name:{order['name']} Order Amount:{order['amount']}")
    
    def total(self):
        print("Total Order Amount:")
        total=sum(order['amount'] for order in self.orders)
        return total

manage_order=CustomerOrder()

manage_order.add_order(1,"Abcd",500)
manage_order.add_order(2,"Bcde",600)
manage_order.add_order(3,"Cdef",700)
manage_order.add_order(4,"Defg",800)

manage_order.print
manage_order.total

