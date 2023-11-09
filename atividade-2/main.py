from category import Category
from product import Product
from client import Client
from order import Order
from orderItem import OrderItem
from socialNetwork import Socialnetwork
from ClientSocialNetwork import ClientSocialnetwork

def main():

    category = Category(1, "Eletrônicos", "Produtos Eletrônicos")

    product = Product("Notebook", "Processador Intel® Core™ de 13ª geração, entregando um rápido e confiável desempenho para mais produtividade.", "07/11/2023", True, category)

    client = Client("Antonio", "Neto", "Rua X", "51984354834", "antonio@email.com", "Masculino")

    order = Order(100.0, "Aprovado", client)

    orderItem = OrderItem(10, 3000, order, product)
    
    print(orderItem)

    socialNetwork = Socialnetwork("@antonioneto", "Instagram")

    clientSocialNetwork = ClientSocialnetwork(client, socialNetwork)

    print(clientSocialNetwork)


if __name__ == "__main__":
    main()