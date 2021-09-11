class FullTurn:
    def __init__(self, turnNum, turnMoves):
        self.turnNum = turnNum
        self.halfturns = {}

        numCharIndexDict = {}
        fullturns = {}
    

class Opening:
  def __init__(self, name, eco, fen, moves):
    self.name = name
    self.eco = eco
    self.fen = fen
    self.moves = moves
  
  def setfullturns(self):
    moves = self.moves
    
    
    halfturns = {}

    

    
    
        ## you hereeee



      
  
    

    #full turns set, separated by space

    #now split into halfturns...
    
  
          
          

class OpeningList:
  items = []

  def __init__(self, items):
    for i in items:
      self.items.append(Opening(**i))
  
  def getOpening(self, moves):
    for i in self.items:
      if(i.moves == moves):
        return i

  def getNextMoves(self):
    pass



  def getPossibleOpenings(self, par):
    possibleItems = []
    for i in self.items:
      if(i.moves.startswith(str(par))):
        i.setfullturns()
        possibleItems.append(i)
      #for i in possibleItems:
        
    return possibleItems