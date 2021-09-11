class Piece:
    def __init__(self, color, id):
        self.color = color
        self.id = id



class Pawn(Piece):
    def __init__(self, color, id):
        Piece.__init__(self, color, id)

    def MakeSet(color):
        set = []
        for i in range(0,8):
            set.append(Pawn(color, i))

        return set

class Rook(Piece):
    def __init__(self, color, id):

        Piece.__init__(self, color, id)

    def MakeSet(color):
        set = []
        for i in range(0,2):
            set.append(Rook(color, i))

        return set

class Knight(Piece):
    def __init__(self, color, id):

        Piece.__init__(self, color, id)

    def MakeSet(color):
        set = []
        for i in range(0,2):
            set.append(Knight(color, i))

        return set

class Bishop(Piece):
    def __init__(self, color, id):

        Piece.__init__(self, color, id)

    def MakeSet(color):
        set = []
        for i in range(0,2):
            set.append(Bishop(color, i))

        return set

class King(Piece):
    def __init__(self, color, id):

        Piece.__init__(self, color, 0)

    def MakeSet(color):
        set = []
        for i in range(0,1):
            set.append(King(color, 0))

        return set

class Queen(Piece):
    def __init__(self, color, id):

        Piece.__init__(self, color, 0)

    def MakeSet(color):
        set = []
        for i in range(0,1):
            set.append(Queen(color, 0))

        return set


