#import TV from Tvclass.py file
from tvClass import TV  

#create Tv1's channel is 30 and volume level is 3
tv1 = TV()
tv1.setChannel(30)
tv1.setVolume(3)

#create Tv2's channel is 3 and volume level is 2
tv2 = TV()
tv2.setChannel(3)
tv2.setVolume(2)

#print the specific output for Tv1 and Tv2 that is given from the problem
#TV1
print("\033[1;36m""=" * 45)
print("\033[1;32m""tv1's channel is", tv1.getChannel(), "\033[1;36m""and " "\033[1;35m" "volume level is", tv1.getVolume())
print("=" * 45)
#TV2
print("\033[1;35m""tv2's channel is", tv2.getChannel(),"\033[1;36m" "and ""\033[1;32m" " volume level is", tv2.getVolume())
print("=" * 45)

