product_names= []
product_prices= []
product_qty= []

while True:
    print("=" *45)
    print("   product inventary system")
    print("=" *45)
    print("1. add product")
    print("2. delete product")
    print("3. update product price")
    print("4. traverse/ display all products")
    print("5. search product (by name)")
    print("6. sort product by price (Assending)")
    print("7.sort product by price (Desending) ")
    print("8.sort product by name (Alphabetical) ")
    print("9.show costlist/ cheapest product ")
    print("10. exit")
    print("=" *45)

    choice = input("enter your choice(1-10): ").strip()

#------add product--------
    if choice == '1':
            name = input("enter product name:").strip()

            if name in product_names:
                  print(f"product'{name} ' already exits! use update option insted.\n")
            else:
                  price = float(input(f"enter price for {name}:"))
                  qty = int(input(f"enter quantity for {name}:"))

                  product_names.append(name)
                  product_prices.append(price)
                  product_qty.append(qty)
                  print(f"product '{name}' added successfully.\n")

    
    elif choice =="2" :
          name = input("enter product name to delete:").strip()

          if name in product_names:
                index = product_names.index(name)
                product_names.pop(index)
                product_prices.pop(index)
                product_qty.pop(index)
                print(f"product'{name}' deleted successfully.\n")
          else:
                print(f"product '{name}' not found.\n") 


    
    elif choice =="3":            
          name = input("enter product name to update price:").strip()

          if name in product_names:
                index = product_names.index(name)
                new_price = float(input(f"enter new price for {name}:"))
                product_prices[index] = new_price
                print(f"price for'{name}' update successfully.\n")

          else:
                print(f"product '{name}' not found.\n")  


    

    elif choice =="4":
          if len(product_names)== 0:
                print("no products to display.\n")

          else:
                print("\n{:<5} {:<20} {:<10}  {:<10}".format("no.", "name", "price", "qty"))      
                print("-" *45)
                for i in range(len(product_names)):
                    print("{:<5} {:<20}   {:<10} {:<30}". format(i+1, product_names[i],product_marks[i], product_qty[i]))
                print()                            


    
    elif choice == "5":
          name = input("enter the product name to search :").strip()

          if name in product_names:
                index = product_names.index(name) 
                print(f"Found -> Name:{product_names[index]},"
                      f"price: {product_prices[index]},Qty: {product_qty[index]}\n")   
          else:
                print(f"product '{name}' not found.\n")          

    
    elif choice == "6":
          if len(product_names) == 0:
                print("no products to sort.\n") 
          else: 

                combined= list(zip(product_prices, product_names, product_qty )) 
                combined.sort()

                product_prices= [item[0] for item in combined]  
                
                product_prices= [item[1] for item in combined]
                product_prices= [item[2] for item in combined]

                print("products sorted by price(ascending).\n")


    
    elif choice == "7":
          if len(product_names) == 0:
                print("no products to sort.\n") 
          else: 
    
                combined= list(zip(product_prices, product_names, product_qty )) 
                combined.sort(reverse=True)
    
                product_prices= [item[0] for item in combined]  
                    
                product_prices= [item[1] for item in combined]
                product_prices= [item[2] for item in combined]
    
                print("products sorted by price(descending).\n")            


    
    
    elif choice == "8":
          if len(product_names) == 0:
                print("no products to sort.\n") 
          else: 
    
                combined= list(zip(product_prices, product_names, product_qty )) 
                combined.sort()
    
                product_prices= [item[0] for item in combined]  
                    
                product_prices= [item[1] for item in combined]
                product_prices= [item[2] for item in combined]
    
                print("products sorted alphabetically by name.\n")                                          
                                    
    
    elif choice == "9":
          if len(product_prices) == 0:
                print("no products available.\n") 
          else:
                highest = max(product_prices) 
                lowest = min(product_prices)

                costliest_index = product_prices.index(highest)
                cheapest_index = product_prices.index(lowest)

                print("\n --------price summary------")
                print(f"costliest product : {product_names[costliest_index]} (price: {highest})")
                print(f"cheapest product : {product_names[cheapest_index]} (price: {lowest})")
                print()

    elif choice == "10" :
          print("exiting program. thank you!")          
          break

    else:
          print("invalid choice. please enter a number between 1 and 10.\n")
