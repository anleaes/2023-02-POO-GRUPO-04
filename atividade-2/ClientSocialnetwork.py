class ClientSocialnetwork:
    
    def _init_(self, client, socialnetwork):
        self.client = client
        self.socialnetwork = socialnetwork

    def _str_(self):
            return f"Cliente: {self.client}, Rede Social: {self.socialnetwork}\n"