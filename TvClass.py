#Michael Angelo P. Biag
#BSCOE 1-4

# Create TV class
class TV:
# constructor
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.power = False

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
    def setChannel(self,channelnumber):
        if channelnumber >= 1 and channelnumber <= 120:
            self.channel = channelnumber

    #Get Volumes
    def getVolume(self):
        return self.volume

    #Set Volume
    def setVolume(self,volumenumber):
        if volumenumber >= 1 and volumenumber <= 7:
            self.volume = volumenumber

    #Channel Up
    def channelUp(self):
        if self.channel < 120:
         self.channel += 1
        else:
         self.channel = 1

    #Channel Dowwn
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
        else:
         self.channel = 120

    #Volume Up
    def volumelUp(self):
        if self.channel < 7:
            self.channel += 1
        else:
            self.channel = 1

    #Volume Down
    def volumeDown(self):
        if self.volume > 1:
            self.volume -= 1
        else:
            self.volume = 7