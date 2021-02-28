import binascii
import math

class LidarData:
    def __init__(self,LSN,FSA,LSA,CS,Angle_correct,Angle_i,Distance_i):
        self.LSN = LSN
        self.FSA = FSA
        self.LSA = LSA
        self.CS = CS

        self.Angle_correct = Angle_correct
        self.Angle_i = Angle_i
        self.Distance_i = Distance_i



def CalcLidarData(str):
    str = str.replace(' ','')

    #print(len(str[16:-4]))

    LSN = int(str[0:4],16)
    FSA = int(str[6:8]+str[4:6],16)
    LSA = int(str[10:12]+str[8:10],16)
    CS = int(str[14:16]+str[12:14],16)

    Angle_correct = list()
    Angle_i = list()
    Distance_i = list()
    count = 0

    for i in range(16,len(str[16:-4]),4):
        count = count + 1

        Distance_i.append(int(str[i+2:i+4]+str[i:i+2],16)>>2)
        if(Distance_i[-1] == 0):
            Angle_correct.append(0)
        else:
            Angle_correct_temp = math.atan(math.radians(19.16*(Distance_i[-1]-90.15)/(90.15*Distance_i[-1])))
            Angle_correct.append(Angle_correct_temp)

        Angle_tmp = (FSA>>1)/64 + ((((LSA>>1)/64) - ((FSA>>1)/64 ))/(LSN-1))*(count-1) - Angle_correct[-1]
        Angle_i.append(Angle_tmp*math.pi/180)
    
    lidarData = LidarData(LSN,FSA,LSA,CS,Angle_correct,Angle_i,Distance_i)
    return lidarData
    
