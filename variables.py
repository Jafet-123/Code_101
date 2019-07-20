#Money in wallet
money_in_wallet = 40
print(money_in_wallet)

#net price of sweets
sweets_price = 7.50
#calculating tax
sales_tax = 0.2 * sweets_price
#calculating gross price 
sweets_price += sales_tax
#updating money in wallet
money_in_wallet -= sweets_price
