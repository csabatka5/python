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

    def power(self) -> None:
        '''
        This function turns the tv on and off by changing
        the value of the status variable.
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        This function mutes and unmutes the tv when it is
        on by changing the value of the muted variable.
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''
        This function increases the tv channel value when the
        tv is on. If the tv is at max channel it will go to
        the minimum channel.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        '''
        This function decreases the tv channel value when the
        tv is on. If the tv is at min channel it will go to
        the maximum channel.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        This function increases the tv volume value when the
        tv is on. If the tv is at max volume it will remain at
        the max volume.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        This function decreases the tv volume value when the
        tv is on. If the tv is at min volume it will remain at
        the min volume.
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
