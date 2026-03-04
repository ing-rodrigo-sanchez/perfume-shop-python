def say_hello(name):
    print(f"Hello {name}, you can buy")


class Sale:
    def __init__(self, name, rut, age):
        self.name = name
        self.rut = rut
        self.age = age
        self.total = 0

    def product(self, price):
        self.total += price

    def ticket(self):
        print(
            "------------------------------- \n",
            f"Customer: {self.name} \n",
            f"RUT:      {self.rut} \n",
            f"Total:    {self.total} \n",
            "------------------------------- \n",
        )


print("Welcome to the perfume shop.")

name = input("Enter your name: ")
rut = input("Enter your rut: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Enter only numbers")

if age >= 18:
    say_hello(name)

else:
    print("You cannot buy")
    exit()

store = {
    1: "Scandal Pour Homme Le Parfum Edp 150Ml - $ 167.990",
    2: "Acqua Di Giò Profondo Parfum 100ml - $ 170.990",
    3: "Bad Boy Cobalt Edp 100 Ml - $ 143.990",
}

print("vailable perfumes:")

for number, product in store.items():
    print(f"{number}. {product}")

print(
    "Enter your number option: \n",
    "To finish adding, type: 0",
)

customer = Sale(name, rut, age)

while True:
    option = int(input())

    if option == 0:
        break

    elif option == 1:
        customer.product(167990)

    elif option == 2:
        customer.product(170990)

    elif option == 3:
        customer.product(143990)

customer.ticket()
