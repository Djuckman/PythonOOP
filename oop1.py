# TODO Написать 3 класса с документацией и аннотацией типов

class Monitor:
    '''
    Class describes computer monitor
    '''
    def __init__(self, monitor_resolution: str, diagonal: int):
        if not isinstance(monitor_resolution, str) or not isinstance(diagonal, int):
            raise TypeError
        if diagonal < 0:
            raise ValueError
        self.monitor_resolution = monitor_resolution
        self.diagonal = diagonal

    def turn_on(self) -> bool:
        '''
        Turns off this Monotor
        If operation has completed successfuly, it returns True, False otherwise

        >>> mon = Monitor("1200x800", 21)
        >>> mon.turn_on()
        True
        '''
        return True

    def power_off(self) -> bool:
        '''
        Turns on this Monotor
        If operation has completed successfuly, it returns True, False otherwise

        >>> mon = Monitor("800x600", 24)
        >>> mon.power_off()
        True
        '''
        return True


class Keyboard:
    '''
    Class describes computer Keyboard
    '''
    def __init__(self, brand: str, size: int):
        if not isinstance(brand, str) or not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError
        self.brand = brand
        self.size = size

    def press_key(self, key_code: int):
        '''
        processes pressed button
        key_code - number value of key code
        Doses not return any value

        :param key_code: str
        '''
        if not isinstance(key_code, int):
            raise TypeError
        pass

    def change_switches(self, switch_type: str):
        '''
        Change switches, for example blue to red
        switch_type - type of switches
        Doses not return any value

        :param switch_type: str
        '''
        if not isinstance(switch_type, str):
            raise TypeError
        if switch_type not in ['red', 'blue', 'black']:
            raise ValueError
        pass


class Mouse:
    '''
    Class describes computer mouse
    '''
    def __init__(self, color: str, mouse_type: str):

        if not isinstance(color, str) or not isinstance(mouse_type, str):
            raise TypeError

        self.possible_colors = ['green', 'blue']
        self.mouse_types = ['optical', 'mech', 'hybrid']

        if color not in self.possible_colors or mouse_type not in self.mouse_types:
            raise ValueError

        self.color = color
        self.mouse_type = mouse_type
        # is meant to be set up be set_up_extra_button method call
        self.extra_button = None

    class ExtraButtonNotSet(Exception):
        pass

    def click_button(self, button_name: str):
        '''
        Is used to emulate button click
        button_name - name of the button
        Doses not return any value

        :param button_name: str
        '''
        if button_name not in ['left', 'right', 'extrabutton']:
            raise ValueError
        if button_name == 'extrabutton':
            if self.extra_button == None:
                raise self.ExtraButtonNotSet()
        pass

    def set_up_extra_button(self, extra_button: str):
        '''
        Is used to configure extra button (define its functionality)
        extra_button - string value to decide its functionality
        Doses not return any value

        :param extra_button: str
        '''
        if not isinstance(extra_button, str):
            raise TypeError
        self.extra_button = extra_button


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
