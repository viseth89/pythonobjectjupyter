import abc
 
# Base Class
 
class AbstractItem(abc.ABC):
    @abc.abstractmethod
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.tax = 1.00
 
    def get_taxed_cost(self):
        taxed_cost = self.cost * self.tax
        return round(taxed_cost, 2)
        # Round Numbers to nearest digit
 
    def get_tax(self):
        difference = self.taxed_cost - self.cost
        return round(difference, 2)
   
# Four Classes that will inherit from Base Class
class DomesticTaxedItem(AbstractItem):
    def __init__(self,name,cost):
        super().__init__(name, cost)
        self.tax += 0.10
 
class DomesticTaxFreeItem(AbstractItem):
    def __init__(self,name,cost):
        super().__init__(name, cost)
        self.tax = 1.00
 
class ImportedTaxedItem(AbstractItem):
    def __init__(self,name,cost):
        super().__init__(name, cost)
        self.tax += 0.15
 
class ImportedTaxFreeItem(AbstractItem):
    def __init__(self,name,cost):
        super().__init__(name, cost)
        self.tax += 0.05
 
# Creation of Global variables outside of class and functions
item_list = []
total = 0
taxtotal = 0
resultstr = ''
 
# exempt = False
# imported = False
 
 
# Handling of Text file,
# We will open the file and create a for loop to read each line-by-line
# From there as each line is read we will slice out information needed such as
# quantity, name and price
# we may create extra variables to turn these strings into floats/integers as needed to perform caclulations or just convert on the fly
# exempt and imported had to be inside for loop?
with open("input3.txt", "r") as f:
    for x in f:
        # Variables inside for loop
        exempt = False
        imported = False
    
        itemname, itemprice = x.split(' at ')
        quantity_characters = [int(s) for s in itemname.split() if s.isdigit()]
        quantity = int(quantity_characters[0])

        # quantity = x[0]
        # iquantity = quantity             # Convert to Integer to be used for math formula
        # originalname = x[1:-6]           # name with 'at'
        # itemname = x[1:-9]               # name without 'at'
        # itemprice = x[-6:]               # Convert to Float to be used for math formula
        fprice = float(itemprice)
    
        # Placed here to test if it is slicing correctly
        print('This is the item : {}'.format(itemname))
        print('Quantity : {}'.format(quantity))
        print('Price : {}'.format(itemprice))
    
        # This is concatening string from opened file to list
        resultstr += (x)
    
        # This is printing the result of the concatened string
        print(resultstr)
    
        arr = ['book', 'chocolate', 'pills', 'chocolates' ]
        if any(item in itemname for item in arr):
            exempt = True
            print('exempt = true : Test to show Cases and Class' ) # test
            
        if 'imported' in itemname:
            imported = True
            print('imported = true : Test to show Cases and Class') # test
        print('--------------------')
        
        if exempt and imported:
            item = ImportedTaxFreeItem(itemname, fprice)
        elif exempt:
            item = DomesticTaxFreeItem(itemname, fprice)
        elif imported:
            item = ImportedTaxedItem(itemname, fprice)
        else:
            item = DomesticTaxedItem(itemname, fprice)
        
        item_list.append(item)
 
print('Summary')
   
totaltaxx = 0
for item in item_list:
#     tax_item = (item.cost)
    totaltaxx += (item.cost)
    print('Each Item Before Tax : ' + str(item.cost))
    print('This is the running total without tax : ' + str(totaltaxx))
 
print('--------------------')
   
 
for item in item_list:
    itemtotal = (item.get_taxed_cost())
    print('Each Item After Tax : ' + str(itemtotal))
    total += itemtotal
    print('This is the running total with tax : ' + str(total))
   
print('This is the total with tax : ' + str(total))
 
print('--------------------')
 
 
tacost = total-totaltaxx
print('Total Tax Amount : ' + str(tacost) )
print(tacost)
print('--------------------------FINAL-------------------------------------------------- ')
print(resultstr)
print('Sales Taxes: ' + str(tacost))
print('Total: ' + str(total))
