#一顆轉好的方塊
FINISHED = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0]]

class cube:
    # 角塊狀態形容：以白、黃為基準，面朝白黃面為0、順時針轉為1、順時針轉兩次為2
    # 邊塊狀態形容：白黃 > 紅橘 > 藍綠，該角塊大的那面如果在大的那面正確則為0，不然則為1
    # 第i個位置目前是第state[i]塊
    # 位置編號以白色面朝上，白紅藍角塊為0，順時針繞一圈再從下一層開始，以黃藍邊塊為19(最後一塊)
    state = list()

    #把方塊轉好
    def init( self ):
        self.state = list( FINISHED )

    #角塊的轉向(plusorminus=1為順時針，plusorminus=-1則為逆時針)
    def corner( num , plusorminus ):
        if plusorminus == 1:
            if num == 0:
                return 1
            if num == 1:
                return 2
            if num == 2:
                return 0
        if plusorminus == -1:
            if num == 0:
                return 2
            if num == 1:
                return 0
            if num == 2:
                return 1

    #邊塊的轉向
    def side( num ):
        if num == 1:
            return 0
        if num == 0:
            return 1

    #所有轉動，共12種
    def spin( self , index):

        #順時針轉動藍色面
        if index == 0:
            temp = self.state[0]
            self.state[0] = [ self.state[12][0] , cube.corner( self.state[12][1] , -1) ]
            self.state[12] = [ self.state[18][0] , cube.corner( self.state[18][1] , 1) ]
            self.state[18] = [ self.state[6][0] , cube.corner( self.state[6][1] , -1) ]
            self.state[6] = [ temp[0] , cube.corner( temp[1] , 1) ]
            temp = self.state[7]
            self.state[7] = self.state[8]
            self.state[8] = self.state[19]
            self.state[19] = self.state[11]
            self.state[11] = temp

        #逆時針轉動藍色面
        if index == 1:
            temp = self.state[18]
            self.state[18] = [ self.state[12][0] , cube.corner( self.state[12][1] , -1) ]
            self.state[12] = [ self.state[0][0] , cube.corner( self.state[0][1] , 1) ]
            self.state[0] = [ self.state[6][0] , cube.corner( self.state[6][1] , -1) ]
            self.state[6] = [ temp[0] , cube.corner( temp[1] , 1) ]
            temp = self.state[7]
            self.state[7] = self.state[11]
            self.state[11] = self.state[19]
            self.state[19] = self.state[8]
            self.state[8] = temp

        #順時針轉動紅色面
        if index == 2:
            temp = self.state[0]
            self.state[0] = [ self.state[2][0] , cube.corner( self.state[2][1] , 1) ]
            self.state[2] = [ self.state[14][0] , cube.corner( self.state[14][1] , -1) ]
            self.state[14] = [ self.state[12][0] , cube.corner( self.state[12][1] , 1) ]
            self.state[12] = [ temp[0] , cube.corner( temp[1] , -1) ]
            temp = self.state[1]
            self.state[1] = [ self.state[9][0] , cube.side( self.state[9][1] ) ]
            self.state[9] = [ self.state[13][0] , cube.side( self.state[13][1] ) ]
            self.state[13] = [ self.state[8][0] , cube.side( self.state[8][1] ) ]
            self.state[8] = [ temp[0] , cube.side( temp[1] ) ]

        #逆時針轉動紅色面
        if index == 3:
            temp = self.state[0]
            self.state[0] = [ self.state[12][0] , cube.corner( self.state[12][1] , 1) ]
            self.state[12] = [ self.state[14][0] , cube.corner( self.state[14][1] , -1) ]
            self.state[14] = [ self.state[2][0] , cube.corner( self.state[2][1] , 1) ]
            self.state[2] = [ temp[0] , cube.corner( temp[1] , -1) ]
            temp = self.state[1]
            self.state[1] = [ self.state[8][0] , cube.side( self.state[8][1] ) ]
            self.state[8] = [ self.state[13][0] , cube.side( self.state[13][1] ) ]
            self.state[13] = [ self.state[9][0] , cube.side( self.state[9][1] ) ]
            self.state[9] = [ temp[0] , cube.side( temp[1] ) ]

        #順時針轉動綠色面
        if index == 4:
            temp = self.state[4]
            self.state[4] = [ self.state[16][0] , cube.corner( self.state[16][1] , -1) ]
            self.state[16] = [ self.state[14][0] , cube.corner( self.state[14][1] , 1) ]
            self.state[14] = [ self.state[2][0] , cube.corner( self.state[2][1] , -1) ]
            self.state[2] = [ temp[0] , cube.corner( temp[1] , 1) ]
            temp = self.state[3]
            self.state[3] = self.state[10]
            self.state[10] = self.state[15]
            self.state[15] = self.state[9]
            self.state[9] = temp

        #逆時針轉動綠色面
        if index == 5:
            temp = self.state[14]
            self.state[14] = [ self.state[16][0] , cube.corner( self.state[16][1] , -1) ]
            self.state[16] = [ self.state[4][0] , cube.corner( self.state[4][1] , 1) ]
            self.state[4] = [ self.state[2][0] , cube.corner( self.state[2][1] , -1) ]
            self.state[2] = [ temp[0] , cube.corner( temp[1] , 1) ]
            temp = self.state[3]
            self.state[3] = self.state[9]
            self.state[9] = self.state[15]
            self.state[15] = self.state[10]
            self.state[10] = temp

        #順時針轉動橘色面
        if index == 6:
            temp = self.state[4]
            self.state[4] = [ self.state[6][0] , cube.corner( self.state[6][1] , 1) ]
            self.state[6] = [ self.state[18][0] , cube.corner( self.state[18][1] , -1) ]
            self.state[18] = [ self.state[16][0] , cube.corner( self.state[16][1] , 1) ]
            self.state[16] = [ temp[0] , cube.corner( temp[1] , -1) ]
            temp = self.state[5]
            self.state[5] = [ self.state[11][0] , cube.side( self.state[11][1] ) ]
            self.state[11] = [ self.state[17][0] , cube.side( self.state[17][1] ) ]
            self.state[17] = [ self.state[10][0] , cube.side( self.state[10][1] ) ]
            self.state[10] = [ temp[0] , cube.side( temp[1] ) ]

        #逆時針轉動橘色面
        if index == 7:
            temp = self.state[4]
            self.state[4] = [ self.state[16][0] , cube.corner( self.state[16][1] , 1) ]
            self.state[16] = [ self.state[18][0] , cube.corner( self.state[18][1] , -1) ]
            self.state[18] = [ self.state[6][0] , cube.corner( self.state[6][1] , 1) ]
            self.state[6] = [ temp[0] , cube.corner( temp[1] , -1) ]
            temp = self.state[5]
            self.state[5] = [ self.state[10][0] , cube.side( self.state[10][1] ) ]
            self.state[10] = [ self.state[17][0] , cube.side( self.state[17][1] ) ]
            self.state[17] = [ self.state[11][0] , cube.side( self.state[11][1] ) ]
            self.state[11] = [ temp[0] , cube.side( temp[1] ) ]

        #順時針轉動白色面
        if index == 8:
            temp = self.state[0]
            self.state[0] = self.state[6]
            self.state[6] = self.state[4]
            self.state[4] = self.state[2]
            self.state[2] = temp
            temp = self.state[1]
            self.state[1] = self.state[7]
            self.state[7] = self.state[5]
            self.state[5] = self.state[3]
            self.state[3] = temp

        #逆時針轉動白色面
        if index == 9:
            temp = self.state[4]
            self.state[4] = self.state[6]
            self.state[6] = self.state[0]
            self.state[0] = self.state[2]
            self.state[2] = temp
            temp = self.state[1]
            self.state[1] = self.state[3]
            self.state[3] = self.state[5]
            self.state[5] = self.state[7]
            self.state[7] = temp

        #順時針轉動黃色面
        if index == 10:
            temp = self.state[12]
            self.state[12] = self.state[14]
            self.state[14] = self.state[16]
            self.state[16] = self.state[18]
            self.state[18] = temp
            temp = self.state[13]
            self.state[13] = self.state[15]
            self.state[15] = self.state[17]
            self.state[17] = self.state[19]
            self.state[19] = temp

        #逆時針轉動黃色面
        if index == 11:
            temp = self.state[12]
            self.state[12] = self.state[18]
            self.state[18] = self.state[16]
            self.state[16] = self.state[14]
            self.state[14] = temp
            temp = self.state[13]
            self.state[13] = self.state[19]
            self.state[19] = self.state[17]
            self.state[17] = self.state[15]
            self.state[15] = temp

    #暴力破解
    def fixxx( self ):

        #計數，供counting使用
        num = 0

        if self.state == FINISHED:
            print("finished!", num)
            return num

        waited = [ self ]

        while 'TRUE':

            #BFS
            for i in range(12):
                temp = cube()
                temp.state = list(waited[0].state)
                temp.spin(i)
                num += 1

                #進度追蹤
                if num % 10000 == 0:
                    print(num)

                #終止條件
                if temp.state == FINISHED:
                    print("finished!", num)
                    return num

                waited.append(temp)

            waited.pop(0)

    #利用fixxx的num回推步驟，透過count回傳
    def counting( self ):
        num = int ( self.fixxx() )
        count = list()

        while num > 0:
            temp = int(num % 12)
            if temp == 0:
                temp = 12
            count.append( temp + ( temp % 2 - 1 ) * 2 )
            num = (num - temp) / 12

        return count

a=cube()
a.init()

for i in [2,10,3,5,7,3,9,2]:
    a.spin(i)

print( a.counting() )
