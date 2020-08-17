'''
Example of using Abstract Factory for cross-platform UI.

'''

from abc import ABC, abstractmethod

class UIElementFactory(ABC):
    '''
    Abstract Factory for UI elements
    '''
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_dropdown(self):
        pass


class AndroidFactory(UIElementFactory):
    def create_button(self):
        return AndroidButton()

    def create_dropdown(self):
        return AndroidDropDown()

class IOSFactory(UIElementFactory):
    def create_button(self):
        return IOSButton()

    def create_dropdown(self):
        return IOSDropDown()


class Button(ABC):
    '''
    Abstract Product
    '''
    @abstractmethod
    def render(self):
        pass

class DropDown(ABC):
    '''
    Abstract Product
    '''
    @abstractmethod
    def render(self):
        pass

class AndroidButton(Button):
    '''
    Concrete Product
    '''
    def render(self):
        print('Rendering Android styled button')


class AndroidDropDown(Button):
    '''
    Concrete Product
    '''
    def render(self):
        print('Rendering Android styled dropdown list')


class IOSButton(Button):
    '''
    Concrete Product
    '''
    def render(self):
        print('Rendering IOS styled Button')


class IOSDropDown(Button):
    '''
    Concrete Product
    '''
    def render(self):
        print('Rendering IOS styled dropdown list')




class ApplicationConfig:
    def __init__(self, OS=None):
        self.OS =  OS or 'Android'

class Client:
    def initialize(self, config):
        if config.OS == 'Android':
            return AndroidFactory()
        elif config.OS == 'IOS':
            return IOSFactory()
        else:
            raise Exception('Error! Unknown Operating System')



if __name__ == "__main__":
    print('App: Launching Android Styled UI')

    config = ApplicationConfig('Android')
    android_ui = Client().initialize(config)
    android_button = android_ui.create_button()
    android_button.render()

    print()

    print('App: Launching IOS Styled UI')
    config = ApplicationConfig('IOS')
    ios_ui = Client().initialize(config)
    ios_button = ios_ui.create_dropdown()
    ios_button.render()
