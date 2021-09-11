class Row:
    def __init__(self, rowNum):
        self.rowNum = rowNum
        self.cells = []


class Cell:
    def __init__(self, cellLett, rowNum, parentRow, id, resxy):
        self.cellLett = cellLett
        self.coords =  str(cellLett) + str(rowNum)
        self.parentRow = parentRow
        self.id = id
        self.rowNum = rowNum

        self.xy = {'x':0, 'y':0}

    #___wider screen cell settings for now, for default 128x64:
        # X:
        self.cellMarginsX = 2   #buys one extra L and R column
        self.width = ((resxy['x'] / 8) - self.cellMarginsX)
        self.xy['x'] = ((Board.LettToNum(self.cellLett) * self.width) - self.width) + self.width

        # Y:
        self.cellMarginsY = 0
        self.height = ((resxy['y'] / 8))
        self.xy['y'] = 56 - ((self.height * self.rowNum) - self.height)

        self.drawableSize = {'x':self.width - 1, 'y':self.height - 1, 'totalpx':(self.height - 1) * (self.width - 1)}

        if(self.rowNum % 2 == 0): #even rows
            if(self.cellLett == 'A' or self.cellLett == 'C' or self.cellLett == 'E' or self.cellLett == 'G'):
                self.color = 'White'
            else:
                self.color = 'Black'
        elif(self.rowNum % 2 == 1): #odd rows
            if(self.cellLett == 'B' or self.cellLett == 'D' or self.cellLett == 'F'     or self.cellLett == 'H'):
                self.color = 'White'
            else:
                self.color = 'Black'

    def ToStr(self):
        strout = "CELL  #" + self.coords + "___________ID:  " + str(self.id) + "\n"
        strout += 'COLOR:  ' + str.capitalize(self.color) + "\t\tXY:  " + str(int(self.xy['x'])) + ", " + str(int(self.xy['y'])) + "\n"
        strout += 'WIDTH/HEIGHT: \t\t' + str(self.width) + 'px/' + str(self.height) + "px\n"
        strout += "MARGINS X/Y:\t\t" + str(self.cellMarginsX) + 'px/' + str(self.cellMarginsY) + "px\n"
        strout += "Drawable size:\t\t" + str(self.drawableSize)
        return strout


#=======================.main.Board.class.========================
class Board:
    def ToStr(self, CELL_XY = 0, HV_LINES = 0):

        #h and v lines option
        if(HV_LINES == 1):
            strout = "\033[4m  |A |B |C |D |E |F |G |H |\033[0m\nhLines:\n"
            for hl in self.hLines:
                strout += str(hl)
                strout += "\n"
            strout += "vLines:\n"
            for vl in self.vLines:
                strout += str(vl)
                strout += "\n"
            return strout

        #xy location option
        if( CELL_XY == 1):
            strout = "\033[4m  |A |B |C |D |E |F |G |H |\033[0m\n"
            for r in self.rows: ###for:
                strout += str(r.rowNum) + "| "
                for c in r.cells:   ###for:
                    strout += '|(' + c.coords + ')' + str(int((c.xy['x']))) + ',' + str(int((c.xy['y'])))
                strout += "\n"
            return strout
    
        #(default) coord Board option:
        strout = "\033[4m  |A |B |C |D |E |F |G |H |\033[0m\n"
        for r in self.rows: ###for:
            strout += str(r.rowNum) + "| "
            for c in r.cells:   ###for:
                strout += c.coords + " "
            strout += "\n"
        return strout

#===============.statics.===============
#todo?
    @staticmethod
    def CellIdToBoardCoord(id):
        pass
    @staticmethod
    def CoordToCellId(coo):
        pass
#
    @staticmethod
    def NumToLett(nn):
        switcher = {1:'A', 2:'B', 3:'C', 4:'D', 5:'D', 6:'F', 7:'G', 8:'H'}
        return switcher.get(nn, " ")
    @staticmethod
    def LettToNum(ll):
        switcher = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
        return switcher.get(ll, " ")
    @staticmethod
    def LettToNumReversed(ll):
        switcher = {'A':8, 'B':7, 'C':6, 'D':5, 'E':4, 'F':3, 'G':2, 'H':1}
        return switcher.get(ll, " ")





#=============.__init__.=============
    def __init__(self, resolution='128x64'):
        self.rows = []
        resxy_ = resolution.split('x')
        self.resxy = {'x':int(resxy_[0]), 'y':int(resxy_[1])  }

        self.Board = []
        idCntr = 0
        for i in reversed(range(1,9)): ###for:
            row = Row(i)
            for c in range(1,9): ###for:
                cell = Cell(Board.NumToLett(c), i, row, idCntr, self.resxy)
                idCntr += 1
                row.cells.append(cell)
            self.rows.append(row)

        #get Boardlines:
        self.hLines = []
        for rr in self.rows:
            cc = rr.cells[0]
            xl = cc.xy['y'] + cc.height - 1
            self.hLines.append( { 'x':0, 'y':xl, 'l':self.resxy['x'], 'c':1 } )
        self.vLines = []
        for rr in self.rows:
            cc = rr.cells[0]
            vl = cc.xy['y'] + cc.width - 1
            self.vLines.append( { 'x':vl, 'y':0, 'l':self.resxy['y'], 'c':1 } )
        
        self.blackCells = []
        self.whiteCells = []
        for r in self.rows:
            for c in r.cells:
                if(c.color == 'White'):
                    self.whiteCells.append(c)
                if(c.color == 'Black'):
                    self.blackCells.append(c)


    #get cell from coords
    def GetCell(self, cd):
        if(len(cd) == 2):
            #let = cd[:1]
            num = int( cd[1:])
            for rw in self.rows:
                if(rw.rowNum == num):
                    for cel in rw.cells:
                        if(cel.coords == cd):
                            return cel