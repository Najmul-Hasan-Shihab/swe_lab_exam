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
    
    def write_to_file(self,filename):
        with open(filename,"w") as file:
            for order in self.orders:
                file.write(f"{order['id']},{order['name']},{order['amount']}")
            print("Orders written.")

    def read_file(self,filename):
        self.orders=[]
        try:
            with open(filename,"r") as file:
                for line in file:
                    order_id,name,amount=line.strip().split(",")
                    self.add_order(order_id,name,float(amount))
                print("Orders read from file.")
        except FileNotFoundError:
                print("File Not Found")


manage_order=CustomerOrder()

manage_order.add_order(1,"Abcd",500)
manage_order.add_order(2,"Bcde",600)
manage_order.add_order(3,"Cdef",700)
manage_order.add_order(4,"Defg",800)

manage_order.print
manage_order.total

