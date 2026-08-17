print("----EXERCISE 2: INVOICE NUMBER PATTERN ---")
frame_rows=int(input("enter frame height(rows):"))
frame_cols=int(input("ente frame width (cols):"))

for i in range(frame_rows):
    for j in range(frame_cols):
        if i == 0 or i == frame_rows - 1:
            print("*", end=" ")
        elif j == 0 or j == frame_cols - 1:
            print("*", end=" ")
        elif i == 1 and j == 12:
            print("RECEIPT", end="")
            break
        else:
            print(" ", end="")
    print()


    print("\n---- OVAL PATTERN ----")

rows = 12
cols = 24

for i in range(rows):
    for j in range(cols):
        x = (j - cols/2) / (cols/2)
        y = (i - rows/2) / (rows/2)

        if x*x + y*y <= 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()