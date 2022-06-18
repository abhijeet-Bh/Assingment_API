class AccessToken:
    access_token = ""

    @staticmethod
    def set_access(token):
        AccessToken.access_token = token

    @staticmethod
    def get_access(self):
        return self.access_token
