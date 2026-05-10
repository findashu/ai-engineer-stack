daily_sales = [500,1000,44,900,77,10]

sumofSalesGT500 = sum(sale for sale in daily_sales if sale > 500)
print(sumofSalesGT500)