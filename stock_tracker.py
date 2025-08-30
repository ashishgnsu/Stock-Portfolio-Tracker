stock_prices={'tata': 130,
    'mrf': 150,
    'asianpaints': 100,
    'puma': 90,
    'nifty': 80,
    'infosys': 1200,
    'reliance': 2500,
    'hdfcbank': 1600,
    'itc': 450,
    'sbi': 600
    }

print("Avialable Stocks: ",list((stock_prices.keys())))

bought_stock=dict()
bool=True
while bool:
    stock_name=  input("Enetr the stock name you want to buy: ").lower()    
    if stock_name in stock_prices.keys():
        stock_quantity= float(input(f"Enter {stock_name} stock quantity you want to buy: "))
        bought_stock.update({stock_name: stock_quantity})
    else:
        print("Stocks are unavilable!!!")
    bool= input("You want to continue buying [yes(Y)/no(N)]: ").lower()
    if bool == 'yes' or bool=='y':
        bool=True
    else:
        bool=False    

total_investment=0
print("total investment stock values: ")   
print(f"{'Stock':<15} | {'Price':<10} | {'Quantity':<10} | {'Investment':<10}")
print("=================================================")
for i in bought_stock.keys():
    print(f"{i:<15}| {stock_prices.get(i):<10}\t| {bought_stock.get(i):<10}\t|{stock_prices.get(i)*bought_stock.get(i):<10}")
    total_investment+=stock_prices.get(i)*bought_stock.get(i)

print("total investemnet by you: ",total_investment)

with open("investment_summary.txt", "w") as f:
    f.write("total investment stock values:\n")
    f.write(f"{'Stock':<15} | {'Price':<10} | {'Quantity':<10} | {'Investment':<10}\n")
    f.write("=================================================\n")
    for i in bought_stock.keys():
        f.write(f"{i:<15}| {stock_prices.get(i):<10}\t| {bought_stock.get(i):<10}\t|{stock_prices.get(i)*bought_stock.get(i):<10}\n")
    f.write("\n")
    f.write("total investemnet by you: " + str(total_investment))
