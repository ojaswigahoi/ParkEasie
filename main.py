import read
import purchase
import write
again="Y"
while again.upper()=="Y":
    a=read.read_file()
    b=purchase.purchase(a)
    write.over_write(a,b)
    again=input("\nDoes any new customer is waiting to park? ")

    print("Are you a shop owner or a customer? Enter 1 or 2.")
    print("1. customer")
    print("2. shop owner")
    person = int(input())
    if person == 1:
        print("Take left from the entry gate")
    else:
        print("Take right from the entry gate")

print("\nThank you for using our app!!")
print("Please check your invoice for your receipt details, \nWhich we created txt file format for you.")

