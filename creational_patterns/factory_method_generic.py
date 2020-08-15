'''Factory Method:
Provides an interface for creating objects, but lets subclasses decide which
class should be instantiated.
'''

from abc import ABC, abstractmethod


class Factory(ABC):
     """
     Factory is an abstract base class. It uses a factory_method that
     will create a product instance. (Creator -> Product)
     """

     @abstractmethod
     def factory_method(self):
         pass

     def factory_function(self):
         product = self.factory_method()
         result = f'Factory - Performing core factory functions using {product.operation()}'

         return result


class ConcreteFactory1(Factory):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteFactory2(Factory):
    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):
    '''
    Product defines all operations concrete products must implement
    '''

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):
    def operation(self):
        return 'Result of concrete product 1 operation'

class ConcreteProduct2(Product):
    def operation(self):
        return 'Result of concrete product 2 operation'



class Client:
    def client_code(self, factory):
        print(f'Client: implementing {factory.factory_function()}')



if __name__ == "__main__":
    print('App: Launched with ConcreteFactory1')
    Client().client_code(ConcreteFactory1())


    print('\nApp: Launched with ConcreteFactory2')
    Client().client_code(ConcreteFactory2())
