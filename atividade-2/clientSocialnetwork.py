class ClientSocialnetwork:

    def __init__(self, client, socialnetwork):
        self.client = client
        self.socialnetwork = socialnetwork

    def __str__(self):
            return f"Cliente: {self.client}, Rede Social: {self.socialnetwork}\n"