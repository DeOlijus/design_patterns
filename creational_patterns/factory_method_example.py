'''
Example of using Factory Method for cross-platform UI.

'''
from abc import ABC, abstractmethod


class BaseButton(ABC):
    ''' Product '''
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, func):
        pass


class WindowsButton(BaseButton):
    ''' Concrete Product '''
    def render(self, *args, **kwargs):
        print(f'Rendering WindowsButton')

    def on_click(self, func):
        # provide logic to handle click event
        print(f'WindowsButton Clicked')
        func()



class HTMLButton(BaseButton):
    ''' Concrete Product '''
    def render(self, *args, **kwargs):
        print(f'Rendering HTMLButton')

    def on_click(self, func):
        # provide logic to handle click event
        print(f'HTMLButton Clicked')
        func()


class BaseDialogBox(ABC):
    ''' Factory '''

    @abstractmethod
    def create_button(self):
        ''' Not primary purpose of factory: To be defined by the subclass '''
        pass
    def type(self):
        return self.__class__.__name__

    def render(self):
        '''
        Primary purpose: To perform core dialog box functions.
        Button creation logic is decoupled from Dialog boxfunctionality.
        '''

        print(f'\nRendering: {self.type()}')
        exit_button = self.create_button()
        exit_button.render()
        exit_button.on_click(self.close_dialog)

    def close_dialog(self):
        print(f'Closing: {self.type()}')


class WindowsDialogBox(BaseDialogBox):
    ''' Concrete Factory '''

    def create_button(self):
        print('Creating: WindowsButton')
        return WindowsButton()


class WebDialogBox(BaseDialogBox):
    ''' Concrete Factory '''

    def create_button(self):
        print('Creating: HTMLButton')
        return HTMLButton()




class Client:
    def initialize(self):
        config = readApplicationConfig()

        if config.OS == 'Windows':
            return WindowsDialogBox()
        elif config.OS == 'Web':
            return WebDialogBox()
        else:
            raise Exception('Error! Unknown Operating System')

class readApplicationConfig:
    def __init__(self):
        self.OS =  'Windows'


if __name__ == "__main__":

    dialog = Client().initialize()
    dialog.render()
