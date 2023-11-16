#Created by Niko Luebbert
import unittest
from television import *

#In order to not defeat the purpose of data hiding, I implemented a getter function I could use for unit testing.
#I could have used the __str__ function to check the program state, but I thought I could create more readable unit tests by using a getter function instead of inferring Television's internal state from str.

class myTestCode(unittest.TestCase):
    def setUp(self):
        #t1 = Television()
        pass
    
    def tearDown(self):
        pass

    def test_init(self):
        t1 = Television()
        self.assertEqual(t1.for_testing_purposes_getter("status"), False)
        self.assertEqual(t1.for_testing_purposes_getter("muted"), False)
        self.assertEqual(t1.for_testing_purposes_getter("volume"), Television.MIN_VOLUME)
        self.assertEqual(t1.for_testing_purposes_getter("channel"), Television.MIN_CHANNEL)

        
    def test_power(self):
        t1 = Television()
        self.assertEqual(t1.for_testing_purposes_getter("status"), False)
        t1.power()
        self.assertEqual(t1.for_testing_purposes_getter("status"), True)
        t1.power()
        self.assertEqual(t1.for_testing_purposes_getter("status"), False)
        
        
    def test_mute(self):
        t1 = Television()
        t1.power()
        #Does mute() toggle the mute varible?
        self.assertEqual(t1.for_testing_purposes_getter("muted"), False)
        t1.mute()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), True)
        t1.mute()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), False)

        #Does changing the volume unmute?
        t1.mute()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), True)
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), False)

        t1.mute()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), True)
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), False)


    def test_channel_up(self):
        #Does it not turn up when it is off?
        t1 = Television()
        t1.channel_up()
        self.assertEqual(t1._Television__channel, Television.MIN_CHANNEL)
        #Will it turn up when it is on?
        t1.power()
        t1.channel_up()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MIN_CHANNEL + 1))
        t1.channel_up()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MIN_CHANNEL + 2))
        t1.channel_up()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MIN_CHANNEL + 3))
        #Did it sucessfully wrap around to the minimum channel?
        t1.channel_up()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), Television.MIN_CHANNEL)
       

    def test_channel_down(self):
    #Does it not go down when it is off?
        t1 = Television()
        t1.channel_down()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), Television.MIN_CHANNEL)
        #Will it go down when it is on?
        t1.power()
        t1.channel_down()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MAX_CHANNEL))
        t1.channel_down()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MAX_CHANNEL - 1))
        t1.channel_down()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), (Television.MAX_CHANNEL - 2))
        #Did it sucessfully wrap around to the maximum channel?
        t1.channel_down()
        self.assertEqual(t1.for_testing_purposes_getter("channel"), Television.MIN_CHANNEL) #same as MAX_CHANNEL - 3
        self.assertEqual(t1.for_testing_purposes_getter("channel"), Television.MAX_CHANNEL - 3)

    def test_volume_up(self):
    #Does it not turn up when it is off?
        t1 = Television()
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("muted"), Television.MIN_VOLUME)
        #Will it turn up when it is on?
        t1.power()
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MIN_VOLUME + 1))
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MIN_VOLUME + 2))
        #Does it do nothing if you try to go over the maximum volume?
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MAX_VOLUME))
        t1.volume_up()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MAX_VOLUME))
        
    def test_volume_down(self):
    #Does it not turn down when it is off?
        t1 = Television()
        t1.power()
        t1.volume_up()
        t1.volume_up()
        t1.volume_up()
        t1.power()
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), Television.MAX_VOLUME)
        #Will it turn down when it is on?
        t1.power()
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MAX_VOLUME -1))
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MAX_VOLUME -2))
        #Does it do nothing if you try to go below the minimum volume?
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MIN_VOLUME))
        t1.volume_down()
        self.assertEqual(t1.for_testing_purposes_getter("volume"), (Television.MIN_VOLUME))
'''
    def test_str(self):
        t1 = Television()
        t1.power()
'''


    

    
