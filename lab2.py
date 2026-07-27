print("--------------Grocery Details--------------")

chips_quantity = float(input("enter the quantity of chips packets:"))
chips_prize_per_packet = 10
chips_total = chips_quantity * chips_prize_per_packet
 
dal_quantity = float(input("enter the quantity of dal in kg:"))
dal_prize_per_kg = 45
dal_total = dal_quantity * dal_prize_per_kg

wheat_quantity = float(input("enter quantity of wheat in kg:"))
wheat_prize_per_kg = 30
wheat_total = wheat_quantity * wheat_prize_per_kg

 
print("------------Grocery Bill Details---------------") 

print("chips: ", chips_total)
print("dal:", dal_total)
print("wheat:", wheat_total)


Total_Bill = chips_total + dal_total + wheat_total
print("Total_Bill :", Total_Bill)

Discount = 0

if Total_Bill>=1000:
    Discount = Total_Bill * 0.5
    print("Discount :", Discount)

elif Total_Bill>= 500:
        Discount = Total_Bill *0.05
        print("Discount :",Discount)    

else :
      print("no Discount")        

Final_Bill = Total_Bill - Discount 

print("Final_Bill :", Final_Bill)
