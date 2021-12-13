num = int(input("Enter a number to find out if its odd or even: "))
def evenOdd():
    calc = num % 2
    if calc <= 0 :
        print(str(num) + " is even")
    if calc > 0:
        print(str(num) + " is odd")

def divisibleBy4():
    calc = num % 4
    if calc == 0 :
        print(str(num)+ " is divisble by 4")
    if calc > 0 :
        print(str(num)+ " is not divisible by 4")



evenOdd()
divisibleBy4()