status = input("Enter Order Status :").lower()
if status=="shipped":
    print("ORDER UPDATE:Your order has been shipped ")
elif status=="delivered":
    print("ORDER UPDATE:Your order has been delivered ")
elif status=="pending":
    print("ORDER UPDATE:Your order has been pending ")
else:
    print("status invalid")