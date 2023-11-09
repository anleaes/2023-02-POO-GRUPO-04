class Order:
    def _init_(self, total_price, status, client):
        self.total_price = total_price
        self.status = status
        self.client = client

    def _str_(self):
            return f"\nPreço Total: {self.total_price}, Status: {self.status}, Cliente: {self.client}\n"