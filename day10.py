#access modifier----public,protected,and private

class gun():
    def __init__(self,name):
        self.name=name #public attributes
        self._name=name #protected
        self.__name=name #private

        ak47=gun("Ak47")
        m4A1=gun("M4A1")
        print(ak47)

            