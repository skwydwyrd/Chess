import pygame
from settings import square_size,piece_width,piece_height
class Piece():
    def __init__(self,image,x,y,type,color):
        self.type=type
        self.color=color
        self.image=image
        self.scaled_width=int(square_size*1)
        self.scaled_height=int((self.scaled_width/piece_width)*piece_height)
        self.image=pygame.transform.scale(self.image,(self.scaled_width,self.scaled_height))
        self.x=x
        self.y=y
        self.selected=None
        self.first_move=True
        self.second_move_done=False

    def update(self,WIN):
        self.draw(WIN)
        self.image=pygame.transform.scale(self.image,(self.scaled_width,self.scaled_height))

    def draw(self,WIN):
        dx=(square_size-self.image.get_width())//2
        dy=(square_size-self.image.get_height())//2
        WIN.blit(self.image,(self.x*square_size+dx,self.y*square_size+dy))

    def draw_at(self,cors,WIN):
        dx=(square_size-self.image.get_width())//2
        dy=(square_size-self.image.get_height())//2
        WIN.blit(self.image,(cors[0]+dx,cors[1]+dy))

class Pawn(Piece):
    def move(self,pieces):
        can_move_to=[]
        if self.color=='white':
            can_move_to.append((self.x,self.y-1))
            if self.first_move:
                can_move_to.append((self.x,self.y-2))

            for piece in pieces:
                #check for diagonal captures
                if piece.color=='black':
                    if (piece.x==self.x+1 and piece.y==self.y-1) or (piece.x==self.x-1 and piece.y==self.y-1):
                        can_move_to.append((piece.x,piece.y))
        else:
            can_move_to.append((self.x,self.y+1))
            if self.first_move:
                can_move_to.append((self.x,self.y+2))
            for piece in pieces:
                #check for diagonal captures
                if piece.color=='white':
                    if (piece.x==self.x-1 and piece.y==self.y+1) or (piece.x==self.x+1 and piece.y==self.y+1):
                        can_move_to.append((piece.x,piece.y))
        for piece in pieces:
            for move in can_move_to:
                if piece.color==self.color:
                    if piece.x==move[0] and piece.y==move[1]:
                        can_move_to.remove(move)
        if not self.first_move:
            self.second_move_done=True
        if self.first_move:
            self.first_move = not self.first_move
        
        return can_move_to

class Rook(Piece):
    def move(self,pieces):
        can_move_to=[]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            for i in range(1,8):
                x,y=self.x+i*dr,self.y+i*dc
                if not (0<=x<8 and 0<=y<8):
                    break
                piece_at_location=next((piece for piece in pieces if piece.x==x and piece.y==y),None)
                if piece_at_location:
                    if piece_at_location.color!=self.color:
                        can_move_to.append((x,y))
                    break
                else:
                    can_move_to.append((x,y))
                if any(piece.x==x and piece.y==y for piece in pieces):
                    break
                can_move_to.append((x,y))
        return can_move_to

class Knight(Piece):
    def move(self,pieces):
        can_move_to=[]
        can_move_to.append((self.x+1,self.y-2))
        can_move_to.append((self.x+2,self.y-1))            
        can_move_to.append((self.x+2,self.y+1))
        can_move_to.append((self.x+1,self.y+2))
        can_move_to.append((self.x-1,self.y+2))
        can_move_to.append((self.x-2,self.y+1))
        can_move_to.append((self.x-2,self.y-1))
        can_move_to.append((self.x-1,self.y-2))
        for piece in pieces:
            for move in can_move_to:
                if piece.color== self.color and piece.x==move[0] and piece.y==move[1]:
                    can_move_to.remove(move)
        return can_move_to

class Bishop(Piece):
    def move(self,pieces):
        can_move_to=[]
        directions=[(1,1),(-1,-1),(-1,1),(1,-1)]
        for dr,dc in directions:
             for i in range(1,8):
                x,y=self.x+i*dr,self.y+i*dc
                if not (0<=x<8 and 0<=y<8):
                    break
                piece_at_location=next((piece for piece in pieces if piece.x==x and piece.y==y),None)
                if piece_at_location:
                    if piece_at_location.color!=self.color:
                        can_move_to.append((x,y))
                    break
                else:
                    can_move_to.append((x,y))
                if any(piece.x==x and piece.y==y for piece in pieces):
                    break
                can_move_to.append((x,y))
        return can_move_to
#TODO: improve the way we add valid moves
class Queen(Piece):
    def move(self,pieces):
        can_move_to=[]
        
        directions=[(1,0),(1,1),(-1,0),(-1,-1),(0,1),(-1,1),(0,-1),(1,-1)]
        for dr,dc in directions:
            for i in range(1,8):
                x,y=self.x+i*dr,self.y+i*dc
                if not (0<=x<8 and 0<=y<8):
                    break
                piece_at_location=next((piece for piece in pieces if piece.x==x and piece.y==y),None)
                if piece_at_location:
                    if piece_at_location.color!=self.color:
                        can_move_to.append((x,y))
                    break
                else:
                    can_move_to.append((x,y))
                if any(piece.x==x and piece.y==y for piece in pieces):
                    break
                can_move_to.append((x,y))
        return can_move_to


    # class King(Piece):
    #     def move(self, pieces, ):
    #         can_move_to = []
    #         can_move_to.extend([(self.x-1,self.y), 
    #                             (self.x-1,self.y-1), 
    #                             (self.x,self.y-1), 
    #                             (self.x+1,self.y-1), 
    #                             (self.x+1,self.y), 
    #                             (self.x+1,self.y+1), 
    #                             (self.x,self.y+1), 
    #                             (self.x-1,self.y+1)])
    #         for piece in pieces:
    #             for move in can_move_to:
    #                 if piece.color!= self.color and piece.x==move[0] and piece.y==move[1]:
    #                     can_move_to.remove(move)

class King(Piece):
    def move(self,pieces):
        can_move_to=[]
        can_move_to.extend([(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1),
							(self.x + 1, self.y + 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1), (self.x - 1, self.y - 1)])
        for piece in pieces:
            for move in can_move_to:
                if piece.color== self.color and piece.x==move[0] and piece.y==move[1]:
                    can_move_to.remove(move)
        return can_move_to
    def get_pos(self):
        return (self.x,self.y)


