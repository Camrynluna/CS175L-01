#Camryn Moschitta
#Professor Eckert
#CS-175L-01
#January 23rd, 2023

#Stocks
Commission_Rate=float(0.03)
Num_Shares=int(2000)
Purchase_Price=float(40.0)
Selling_Price=float(42.75)

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
