'''Abstract Factory:
Provides an interface for creating families of related or dependent objects without
specifying their concrete classes
'''


from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    '''
    Defines all product familes a concrete factory must create
    '''
    @abstractmethod
    def create_product_family_a(self):
        '''
        Returns abstract product family A
        '''
        pass

    @abstractmethod
    def create_product_family_b(self):
        '''
        Returns abstract product family B
        '''
        pass

class AbstractProductFamilyA(ABC):
    '''
    Defines the core methods all products of Family-A must implement
    '''
    @abstractmethod
    def core_function_a(self):
        pass


class AbstractProductFamilyB(ABC):
    '''
    Defines the core methods all products of Family-B must implement
    '''
    @abstractmethod
    def core_function_b(self):
        pass

    @abstractmethod
    def other_core_function_b(self, compatible_product):
        '''
        Families of products can also interact with other 'compatible' products
        that are of the same model
        '''
        pass


class Concrete_Model1_Factory(AbstractFactory):
    '''
    Defines all product families that will be created in the model 1 style
    '''

    def create_product_family_a(self):
        '''
        Returns a model 1 styled product in the A family
        '''
        return Concrete_ProductFamilyA_model1()


    def create_product_family_b(self):
        '''
        Returns a model 1 styled product in the B family
        '''
        return Concrete_ProductFamilyB_model1()


class Concrete_Model2_Factory(AbstractFactory):
    '''
    Defines all products families that will be created in the model 2 style
    '''
    def create_product_family_a(self):
        '''
        Returns a model 2 styled product in the A family
        '''
        return Concrete_ProductFamilyA_model2()


    def create_product_family_b(self):
        '''
        Returns a model 2 styled product in the B family
        '''
        return Concrete_ProductFamilyB_model2()


class Concrete_ProductFamilyA_model1(AbstractProductFamilyA):
    '''
    Defines the core functions of a model 1 styled product in the A family
    '''
    def core_function_a(self):
        return 'Result of Family A model 1 product\'s core function.'


class Concrete_ProductFamilyB_model1(AbstractProductFamilyB):
    '''
    Defines the core functions of a model 1 styled product in the B family
    '''
    def core_function_b(self):
        return 'Result of Family B model 1 product\'s core function.'

    def other_core_function_b(self, compatible_product):
        '''
        Compatible product must be of same model type to be compatible
        and will only work with families that are of Model 1 type here.
        '''
        result = compatible_product.core_function_a()
        return f'Result of other Core Function of Family B model 1 product - '\
        f'\n\treturning result of compatible product: {result}'



class Concrete_ProductFamilyA_model2(AbstractProductFamilyA):
    def core_function_a(self):
        return 'Result of Family A model 2 product\'s core function.'


class Concrete_ProductFamilyB_model2(AbstractProductFamilyB):
    def core_function_b(self):
        return 'Result of Family B model 2 product\'s core function.'

    def other_core_function_b(self, compatible_product):
        '''
        Will only work with families that are of Model 2 type.
        '''
        result = compatible_product.core_function_a()
        return f'Result of other Core Function of Family B model 2 product - '\
        f'\n\treturning result of compatible product: {result}'


class Client:
    def client_code(self, factory):
        '''
        The Abstract Factory pattern ensures the model type is the same at creation.
        The Client uses the Factory model passed in to create products of various
        families of the same model type ensuring compatibility
        '''
        product_a = factory.create_product_family_a()
        product_b = factory.create_product_family_b()

        print(f'Client - implementing core function of product_b:',
        f'{product_b.core_function_b()}')

        print(f'Client - implementing other core function of product_b: ',
        f'{product_b.other_core_function_b(product_a)}')



if __name__ == "__main__":
    print('App: Launched with Concrete_Model1_Factory')
    Client().client_code(Concrete_Model1_Factory())


    print('\nApp: Launched with Concrete_Model2_Factory')
    Client().client_code(Concrete_Model2_Factory())
