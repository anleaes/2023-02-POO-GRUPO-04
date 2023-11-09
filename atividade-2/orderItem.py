class OrderItem:

    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.order = order
        self.product = product

    def __str__(self):
            return f"\nQuantidade: {self.quantity} \nPreço Unitario: {self.unitary_price} \nProduto: {self.product} \nOrder: {self.order}\n"