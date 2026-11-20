from functools import reduce
products=[("laptop",45000),("mouse",500),("keyboard",1500),("monitor",4000),("headphones",2500)]
#filter product under rupees 5000
filter_product=list(filter(lambda product: product[1]<5000,products))
print(filter_product)
#15% discount using map()
discounted_products=list(map(lambda product:(product[0], product[1]*0.85),filter_product))
print(discounted_products)
#total discounted value using reduce()
total=reduce(lambda a,b: a+b[1], discounted_products,0)
print(total)


#employee salary analyzer
from functools import reduce
employees=[("rahul",25000),("priya",35000),("amit",45000),("neha",3000),("sneha",50000)]
filter_employees=list(filter(lambda employee: employee[1]>30000,employees))
print(filter_employees)
increment=list(map(lambda employee: (employee[0],employee[1]*1.10),filter_employees))
print(increment)
sorted_employees=sorted(increment,key=lambda employee: employee[1])
print(sorted_employees)
total=reduce(lambda a,b: a+b[1],sorted_employees,0)
print(total)