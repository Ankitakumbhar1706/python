status = input("Enter Atmospheric Status :").lower()
if status=="hot":
    print("turn on AC ")
elif status=="cold":
    print("Activate Heater ")
elif status=="normal":
    print("idle ")
else:
    print("status invalid")