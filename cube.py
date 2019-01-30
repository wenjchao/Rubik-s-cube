class cube:
    # 角塊狀態形容：以白、黃為基準，面朝白黃面為0、順時針轉為1、順時針轉兩次為2
    # 邊塊狀態形容：白黃 > 紅橘 > 藍綠，該角塊大的那面如果在大的那面正確則為0，不然則為1
    # 第i個位置目前是第state[i]塊
    state=[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0]]

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

    #順時針轉動藍色面
    def blue( self ):
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
    def antiblue( self ):
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


a=cube()
a.blue()
print(a.state)
a.antiblue()
print(a.state)
