'''
# def saveThePrisoner(n, m, s):
#     start=s
#     while m!=0:
#         if start>n:
#             start=1
#         start+=1
#         m-=1
#     return start-1
def saveThePrisoner(n, m, s):
    return n if (m+s-1)%n==0 else (m+s-1)%n
print(saveThePrisoner(3,7,3))'''
class VendingMachine:
    def __init_(self, num_items, item_price):
        self.num_items =num_items
        self.item_price =item_price
    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        cost=req_items*self.item_price
        if money < cost:
            raise ValueError("Not enough coins")
        change=money-cost
        self.num_items -=req_items
        return change