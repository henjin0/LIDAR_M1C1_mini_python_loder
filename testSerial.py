import serial
import binascii
from CalcLidarData import CalcLidarData
import matplotlib.pyplot as plt
import math

#b = binascii.a2b_hex('AAAAAAAA'+'01'+'12'+'0000'+'0000'+'13')

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('lidar ',fontsize=18)
#plt.show()

ser = serial.Serial(port='/dev/tty.usbserial-1420',
                    baudrate=115200,
                    timeout=5.0,
                    bytesize=8,
                    parity='N',
                    stopbits=1)
#ser.write(b)
tmpString = ""
aaFlag = False

for i in range(100):
    loopFlag = True

    while loopFlag:
        b = ser.read()

        tmpInt = int.from_bytes(b, 'big')
        if(tmpInt == 0xAA):
            aaFlag = True
            tmpString += b.hex() + " "
        elif(tmpInt == 0x55 and aaFlag):
            aaFlag = False
            tmpString += b.hex()
            #print(tmpString)

            if(int(tmpString[0:2],16)==0x00 and int(tmpString[3:5],16)==0x19):
                lidarData = CalcLidarData(tmpString)
                #print(lidarData.Distance_i)
                ax.scatter(lidarData.Angle_i, lidarData.Distance_i)
                ax.set_theta_offset(math.pi / 2)
                
            tmpString = ""
            loopFlag = False
        else:
            aaFlag = False
            tmpString += b.hex()+" "

plt.show()
ser.close()