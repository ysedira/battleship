
from Position import Position
from Grid import Grid

class TextDisplay:

    @staticmethod    
    def draw(board, ships=None, showShips=False):
        def helperDrawHorizLine(l):
            output = '+'
            for i in range(l):
                output += '---+'
            print output

        #raise NotImplemented
        missedPos = board.getMissedPositions()
        hitPos = board.getHitPositions()
        for h in range(board.height):
            helperDrawHorizLine(board.width)
            rowOutput = "|"
            for w in range(board.width):
                pos = Position(w, h)
                if pos in missedPos:
                    rowOutput += ' o ' 
                elif pos in hitPos:
                    rowOutput += ' x '
                elif showShips and ships is not None:
                    hasShip = False
                    for ship in ships:
                        if ship.hasShip(pos):
                            hasShip = True
                    if hasShip:
                        rowOutput += ' . '
                    else:
                        rowOutput += '   '    
                else:
                    rowOutput += '   ' 
                rowOutput += '|'
            print rowOutput
        helperDrawHorizLine(board.width)  
 