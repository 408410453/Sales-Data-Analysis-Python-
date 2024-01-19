import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# (三)(五)total revenue for each product & Best Performing Product
def Total_Revenue_and_Beat_Product(df_new):
    #total revenue for each product 
    Product = {
        "Product_A":0,
        "Product_B":0
    }
    
    for i in range(len(df_new)):
        if df_new.at[df_new.index[i],"Product"] == "Product  A":
            Product["Product_A"]+=int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
        elif df_new.at[df_new.index[i],"Product"] == "Product  B":
            Product["Product_B"]+=int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])

    #Best Performing Product
    max=0
    if Product["Product_A"]>Product["Product_B"]:
        max = "Product_A"
    else:
        max = "Product_B"

    return Product,max

#(四)(六)Monthly Sales Report & Plotting
def Monthly_Sales_and_Plotting(df_new):
    #Monthly Sales Report 
    #US -> Units Sold   RE -> Total Revenue
    Month_Sales = {
        "date_month":[1,2,3,4,5,6,7,8,9,10,11,12],
        "product_A_US":[0,0,0,0,0,0,0,0,0,0,0,0],
        "product_B_US":[0,0,0,0,0,0,0,0,0,0,0,0],
        "product_A_RE":[0,0,0,0,0,0,0,0,0,0,0,0],
        "product_B_RE":[0,0,0,0,0,0,0,0,0,0,0,0],
    }
    Month_Sales= pd.DataFrame(Month_Sales)

    for i in range(len(df_new)):
        match pd.DatetimeIndex(df_new['Date']).month[df_new.index[i]]:
            case 1:
                if df_new.at[df_new.index[i],"Product"] == "Product  A":
                    Month_Sales.at[0,"product_A_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[0,"product_A_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
                elif df_new.at[df_new.index[i],"Product"] == "Product  B":
                    Month_Sales.at[0,"product_B_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[0,"product_B_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
            case 2:
                if df_new.at[df_new.index[i],"Product"] == "Product  A":
                    Month_Sales.at[1,"product_A_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[1,"product_A_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
                elif df_new.at[df_new.index[i],"Product"] == "Product  B":
                    Month_Sales.at[1,"product_B_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[1,"product_B_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
            case 3:
                if df_new.at[df_new.index[i],"Product"] == "Product  A":
                    Month_Sales.at[2,"product_A_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[2,"product_A_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
                elif df_new.at[df_new.index[i],"Product"] == "Product  B":
                    Month_Sales.at[2,"product_B_US"]+= int(df_new.at[df_new.index[i],"Units Sold"])
                    Month_Sales.at[2,"product_B_RE"]+= int(df_new.at[df_new.index[i],"Units Sold"])*int(df_new.at[df_new.index[i],"Unit Price"])
    labels= [int(i) for i in range(1,len(Month_Sales)+1)]

    #Plotting
    plt.xticks(ticks=Month_Sales["date_month"],labels=labels,) 
    plt.xlabel("Month_Sales", fontsize=20)
    plt.ylabel('Total Revenue', fontsize=20)
    plt.title("Bule:product_A  Red:product_B",loc='left')
    plt.bar(Month_Sales["date_month"]-0.2,Month_Sales["product_A_RE"],width=0.4,color='b')
    plt.bar(Month_Sales["date_month"],Month_Sales["product_B_RE"],align='edge',width=0.4,color='r')
    plt.show()
              
    return Month_Sales


with open('sales_data.csv','r',encoding='utf-8') as cvsfile:
    
    #(一)Read Data
    rows = csv.reader(cvsfile) 
    df = pd.DataFrame(rows)
    df.columns = ["Date","Product","Units Sold","Unit Price","Total Revenue"]

    #(二)Data Cleaning
    df_new = df.dropna()
    print(df_new)

    # (三)(五)total revenue for each product & Best Performing Product
    print(Total_Revenue_and_Beat_Product(df_new))

    #(四)(六)Monthly Sales Report & plotting
    print( Monthly_Sales_and_Plotting(df_new))

    
    
    
    

   


    
  

            
