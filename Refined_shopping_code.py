class Shopping:
    def __init__(self):
        self.item = {}
        self.list_of_item= {"Mysor_silk_saree":9000,
                "Lehanga":5000,
                "Jeans":2000,
                "Jacket":700,
                "Dress":900,
                "Salwar_Kameez":2500
                }
        for key,value in self.list_of_item.items():    
            print(f"{key}:{value}")
        s = input("Enter the item seperated by comma: \n")
        selected_item = s.split(",")
        for i in selected_item:
            i = i.strip()
            if i in self.list_of_item:
                
                self.item[i]= self.list_of_item[i]
            else:
                print(f"{i} not found")
        print(f"Selected Item : {self.item}")
        
    def Total_amount(self):

        self.total = 0
        for i in self.item:
            self.total += self.item[i]
        return self.total   
    #  print(f"Total Amount : {self.total}")
    def Discount(self,percentage_of_discount):
        self.percentage_of_discount = percentage_of_discount
        if self.total>=5000:
            self.total-=(self.total*(self.percentage_of_discount/100))
        else:
            self.total = self.total
class Tax(Shopping):
    
    def calculate_tax(self,tax_amount):
        self.Total_amount()

        if self.total <= 1000:
            tax = 0.025
        elif self.total<=5000:
            tax = 0.05
        else:
            tax = tax_amount
        final_amount = self.total+(self.total*tax)
        self.amount = final_amount
    def display_bill(self):
        print(f"Final amount you had to pay is : {self.amount}")
        
sam = Tax()
sam.Total_amount()
sam.Discount(10)
sam.calculate_tax(0.1)
sam.display_bill()