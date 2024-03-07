
'''
A. Create a function named calculate_discount(price, discount_percent) that calculates 
the final price after applying a discount. The function should take the original price 
(price) and the discount percentage (discount_percent) as parameters. If the discount is 
20% or higher, apply the discount; otherwise, return the original price.
'''
# Function with pre keyed in values
def calculate_discount(price, discount_percent):
    discount_price = 0.0
    if(discount_percent >= 0.2):
        discount_price = price*discount_percent
    return price - discount_price
print("Function called with pre keyed in values")      
print("Price after discount applied is:_", calculate_discount(500.0,0.2))


'''
B. Using the calculate_discount function, prompt the user to enter the original price of an 
item and the discount percentage. Print the final price after applying the discount, or if no 
discount was applied, print the original price.

'''
print("==============================================")
print("Enter values for price and discount percentage")
#Key in values for price and discount

price = float(input("Enter item price:_"))
discount_percent = (float(input("Enter discount percentage e.g 30:_")))/100

if(discount_percent == 0.0):
    # Return the entered price if no discount entered
    discount_percent = 1
    #calculate_discount(price,discount_percent)
    print("Price without discount applied is :_", price)
else:
    calculate_discount(price,discount_percent)
    
# Call the function with the user supplied values
    print("Function called with user supplied values via keyboard")
    print(calculate_discount(price,discount_percent))


