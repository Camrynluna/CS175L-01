#Camryn Moschitta
#Professor Eckert
#CS-175L-01
#January 23rd, 2023

#stocks
Commission_Rate=float(input('Commission rate for the purchase: ')) 
Num_Shares=int(input('Number of shares purchased: '))
Purchase_Price=float(input('Price of the purchase: '))
Selling_Price=float(input('Selling price of the purchase: '))

amountPaidForStock=Num_Shares*Purchase_Price
purchaseCommission=Commission_Rate*amountPaidForStock
totalPaid=amountPaidForStock+purchaseCommission
stockSoldFor=Num_Shares*Selling_Price
sellingCommission=Commission_Rate*stockSoldFor
totalReceived=stockSoldFor-sellingCommission
profitOrLoss=totalReceived-totalPaid

print("Amount paid for stock:$",amountPaidForStock)
print("Commission paid on the purchase:$",purchaseCommission)
print("Amount the stock sold for:$",stockSoldFor)
print("Commission paid on the sale:$",sellingCommission)
print("Profit (or loss if negative):$",profitOrLoss)
