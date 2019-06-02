nm = int(input("Enter Number:"))
for e in range(1,nm-1):
    if (nm % e)==0:
        print(e, "devides by", nm)
