class itemz:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

    def getTotal(self):
        return self.price * self.qty

    def getTMostPrices(self):
        return self.price * self.qty * 0.6

    def calculateEnvFee(self):
        if self.category == "electronics":
            return 5 * self.qty
        return 0


class shoppinCart:
    def __init__(self):
        self.items = []
        self.taxRate = 0.08
        self.memberDiscount = 0.05
        self.bigSpenderDiscount = 10
        self.couponDiscount = 0.15
        self.currency = "USD"

    def addItem(self, item):
        self.items.append(item)

    def calculateSubtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += item.getTotal()
        return subtotal

    def applyDiscounts(self, subtotal, isMember):
        if isMember:
            subtotal -= (subtotal * self.memberDiscount)

        if subtotal > 100:
            subtotal -= self.bigSpenderDiscount
        return subtotal

    def calculateTotal(self, isMember, hasCoupon):
        subtotal = self.calculateSubtotal()

        # Calcular tarifas ambientales
        env_fee = sum(item.calculateEnvFee() for item in self.items)
        subtotal += env_fee

        subtotal = self.applyDiscounts(subtotal, isMember)
        total = subtotal + (subtotal * self.taxRate)

        if hasCoupon == "YES":
            total -= (total * self.couponDiscount)
        return total


def main():
    cart = shoppinCart()
    items_data = [
        ("Apple", 1.5, 10),
        ("Banana", 0.5, 5),
        ("Laptop", 1000, 1)
    ]

    for name, price, qty in items_data:
        if price < 0 or qty < 0:
            print("Error: El precio y la cantidad deben ser no negativos.")
            return

        item = itemz(name, price, qty)
        if name == "Laptop":  # Asignar categoría para la laptop
            item.category = "electronics"
        cart.addItem(item)

    isMember = True
    hasCoupon = "YES"
    try:
        total = cart.calculateTotal(isMember, hasCoupon)
        if total < 0:
            print("Error en el cálculo!")
        else:
            print(f"El precio total es: ${total:.2f}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
