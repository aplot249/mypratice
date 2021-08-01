class classonlymethod(classmethod):
    def __get__(self, instance, cls=None):
        if instance is not None:
            raise AttributeError("This method is available only on the class, not on instances.")
        return super().__get__(instance, cls)

class Fu:
    @classonlymethod
    def as_view(cls):
        print(cls.__name__)
        print("这是as_view方法")

class Zi(Fu):
    def run(self):
        print("这是run方法")

Zi.as_view()