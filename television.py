#Created by: Niko Luebbert
from typing import Union #For the type hinting of the getter function I used for the tests
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        #self.__print_volume: Int

    #(https://www.blog.pythonlibrary.org/2021/09/11/python-3-10-simplifies-unions-in-type-annotations/)
    #This getter can return either an integer or a boolean. The version of Python on my computer was 3.8.10 instead of 3.10, and therefore I used Union[] to hint two possible return types.
    def for_testing_purposes_getter(self, vname) -> Union[int, bool]:
        if vname == "status":
            return self.__status
        elif vname == "muted":
            return self.__muted
        elif vname == "volume":
            return self.__volume
        elif vname == "channel":
            return self.__channel
            

    def __tv_is_off(self) -> Union[bool, None]:
        '''
        Returns True if the tv is off.
        :return: True if self.__status == False
        '''
        if self.__status == False: #(status == false means tv is off.)
            #print("returned because off")
            return True
        

    def power(self) -> None:
        '''
        Changes the Television from on to off and vice versa.
        '''
        self.__status = not self.__status #change self.status to it's current opposite.

    def mute(self) -> None:
        '''
        Changes the mute feature of the TV from on to off and vice versa.
        Note that sucessfully running volume_up() or volume_down() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__tv_is_off() == True: #stop function if tv is currently turned off
            return
        
        self.__muted = not self.__muted #change self.muted to it's current opposite.

    def channel_up(self) -> None:
        '''
        Increases the channel number by 1.
        Note that attempting to increase the channel number past MAX_CHANNEL will cause the channel number to wrap around to MIN_CHANNEL.

        This function does nothing if the Television is off.
        '''
        if self.__tv_is_off() == True: #stop function if tv is currently turned off
            return
        
        
        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL #wrap channel around if you go over max.
        else:
            self.__channel += 1
            


    def channel_down(self) -> None:
        '''
        Decreases the channel number by 1.
        Note that attempting to decrease the channel number below MIN_CHANNEL will cause the channel number to wrap around to MAX_CHANNEL.

        This function does nothing if the Television is off.
        '''
        if self.__tv_is_off() == True: #stop function if tv is currently turned off
            #print("cant channel down because tv is off.")
            return
        
        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL #wrap channel around if you go below minimum.
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Increases the volume by 1.
        Note that attempting to increase the volume beyond MAX_VOLUME will not change the volume.
        Note that sucessfully running volume_up() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__tv_is_off() == True: #stop function if tv is currently turned off
            return
        
        self.__muted = False #unmute if not already unmuted
        if self.__volume != Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        '''
        Increases the volume by 1.
        Note that attempting to increase the volume below MAX_VOLUME will not change the volume.
        Note that sucessfully running volume_down() will automatically unmute the TV.

        This function does nothing if the Television is off.
        '''
        if self.__tv_is_off() == True: #stop function if tv is currently turned off
            return
        
        self.__muted = False #unmute if not already unmuted
        if self.__volume != Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns a status report including whether the Television is on, the current channel, and the current volume.
        Note that the volume will register as 0 if the TV is muted.
        :return: f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__print_volume}]'
        '''
        if self.__muted == True:
            self.__print_volume = 0
        else:
            self.__print_volume = self.__volume

        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__print_volume}]'
        

    
