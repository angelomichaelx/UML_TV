#Michael Angelo P. Biag
#BSCOE 1-4

# Create TV class
class TV:
# constructor
    def __init__(self, channel = 1, volume = 1, power = False):
        self.channel = channel
        self.volume = volume
        self.power = power

#Methods

#Turn On
def turnOn(self):
    self.power = True
#Turn Off
def turnOff(self):
    self.power = False
#Get Channel 
def getChannel(self):
    return self.channel 
#Set Channel 
def setChannel(self,channel):
    if channel >= 1 and channel <= 120:
        self.channel = channel
#Get Volumes
def getVolume(self):
    return self.volume
#Set Volume
def setVolume(self,volume):
        if volume>=1 and volume<=7:
            self.volume=volume
#Channel Up
def channelUp(self):
     if self.channel<120:
        self.channel+=1
     else:
        self.channel=1

#Channel Dowwn

#Volume Up

#Volume Down
