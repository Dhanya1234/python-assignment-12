dict = {'a': 100, 'b':200, 'c':300} 
def returnSum(dict): 
     sum = 0
     for i in dict.values(): 
         sum = sum + i 
     return sum
print("Sum :", returnSum(dict)) 