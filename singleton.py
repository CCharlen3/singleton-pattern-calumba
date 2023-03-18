class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton exists already!")
        else:
            Singleton.__instance = self


s1 = Singleton.getInstance()
s2 = Singleton.getInstance()
print(s1 == s2)
