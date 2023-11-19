#Created by Niko Luebbert
import unittest
from television import *

#I have rewritten my unit tests to use the __str__ function instead of a getter.

class myTestCode(unittest.TestCase):
    def setUp(self):
        #t1 = Television()
        pass
    
    def tearDown(self):
        pass

    def test_init(self):
        t1 = Television()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
                         
      
    def test_power(self):
        t1 = Television()

        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        t1.power()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        t1.power()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        

    def test_mute(self):
        t1 = Television()
        t1.power()
        #the tv is on, the volume is increased once, and then the tv is muted:
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 1")
        t1.mute()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        #The tv is on and unmuted:
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 2")
        #tv is off and muted:
        t1.mute()
        t1.power()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #tv is off and unmuted:
        t1.power()
        t1.volume_down()
        t1.power()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        #tv is off and channel tries to increase:
        t1 = Television()
        t1.channel_up()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #tv is on and the channel increases:
        t1.power()
        t1.channel_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 1, Volume = 0")
        #increasing past the maximum channel:
        t1.channel_up()
        t1.channel_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 3, Volume = 0")
        t1.channel_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")

        
        
    def test_channel_down(self):
        #Does it not go down when it is off?
        t1 = Television()
        t1.channel_down()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #Does it decrease and wrap around when it is on?
        t1.power()
        t1.channel_down()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 3, Volume = 0")
    


    def test_volume_up(self):
        #Does it not turn up when it is off?
        t1 = Television()
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        #Does it turn up when it is on?
        t1.power()
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 1")
        #What about when it is on, muted, and the volume is increased?
        t1.mute()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 2")
        #What if you try to go over the maximum volume?
        t1.volume_up()
        t1.volume_up()
        t1.volume_up()
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 2")
        

    def test_volume_down(self):
        #The tv is off and the volume is decreased:
        t1 = Television()
        t1.volume_down()
        self.assertEqual(t1.__str__(), "Power = False, Channel = 0, Volume = 0")
        t1.power()
        #Increasing volume to maximum to prepare for test:
        t1.volume_up()
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 2")
        #When the tv is on and the volume is decreased:
        t1.volume_down()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 1")
        t1.volume_down()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        #Increasing volume to maximum to prepare for another test:
        t1.volume_up()
        t1.volume_up()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 2")
        t1.mute()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 0")
        t1.volume_down()
        self.assertEqual(t1.__str__(), "Power = True, Channel = 0, Volume = 1")
                
'''
    def test_str(self):
        t1 = Television()
        t1.power()
        
'''


    

    
