from login import urlconfig


class Qzone:

    def __init__(self,name,password):
        self.name=name
        self.password=password

    def prelogin(self):
        preloginUrl=urlconfig.preLoginUrl
