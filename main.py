import pygame
from piece import Pawn,Rook,Knight,Bishop,Queen,King

from board import Board
from player import Player
from settings import *

pygame.init()



piece_classes={
    "pawn":Pawn,
    "rook":Rook,
    "knight":Knight,
    "bishop":Bishop,
    "queen":Queen,
    "king":King,

}
pieces=[]
for row,row_layout in enumerate(pieces_layout):
    for col,piece in enumerate(row_layout):
        color='white' if row>4 else 'black'
        pieces.append(piece_classes[piece](pieces_data[f'{color}_{piece}'],col,row,piece,color))

def create_text():
    font = pygame.font.Font('freesansbold.ttf', 30)

    p1 = font.render('Player 1: Black', True, BLACK)
    rectp1 = p1.get_rect()
    rectp1.topleft = (820, 20)

    p2 = font.render('Player 2: White', True, BLACK)
    rectp2 = p2.get_rect()
    rectp2.topleft = (820, 420)

    castle_p1 = font.render('CASTLE', True, BLACK)
    rect_castle_p1 = castle_p1.get_rect()
    rect_castle_p1.topleft = (820, 60)

    castle_p2 = font.render('CASTLE', True, BLACK)
    rect_castle_p2 = castle_p2.get_rect()
    rect_castle_p2.topleft = (820, 460)

    in_check_p1 = font.render('CHECK', True, BLACK)
    in_check_rect_p1 = in_check_p1.get_rect()
    in_check_rect_p1.topleft = (820, 100)

    in_check_p2 = font.render('CHECK', True, BLACK)
    in_check_rect_p2 = in_check_p2.get_rect()
    in_check_rect_p2.topleft = (820, 500)

    return p1, rectp1, p2, rectp2, castle_p1, rect_castle_p1, castle_p2, rect_castle_p2, in_check_p1, in_check_rect_p1, in_check_p2, in_check_rect_p2

# this order: p1, rectp1, p2, rectp2, castle_p1, rect_castle_p1, castle_p2, rect_castle_p2, in_check_p1, in_check_rect_p1, in_check_p2, in_check_rect_p2
text= create_text()

def is_in_check(king_color,pieces):
    '''king_color is color of checked king, maybe'''
    #find king pos

    king = next((piece for piece in pieces if isinstance(piece, King) and piece.color == king_color), None)
    king_pos = king.get_pos()
    print(king,king_pos)

    #check if opposing piece can capture king
    for piece in pieces:
        if king_pos in piece.move(pieces):
            return True
    return False
def handle_mouse_down(event, pieces, board, current_turn):
    """Handle MOUSEBUTTONDOWN events."""
    mouseX, mouseY = event.pos
    col = mouseX // square_size
    row = mouseY // square_size
    for piece in pieces:
        if (piece.x == col and piece.y == row) and (piece.color==current_turn):
            return piece, piece.move(pieces), (piece.x, piece.y), event.pos
    return None, [], None, None

def handle_mouse_up(event, dragging, selected_piece, original_pos, available_moves, pieces, pw, pb, current_turn):
    """Handle MOUSEBUTTONUP events."""

    if not dragging:
        return current_turn
    mouseX, mouseY = event.pos
    col = mouseX // square_size
    row = mouseY // square_size
    if (col, row) in available_moves:
        selected_piece.x = col
        selected_piece.y = row
        # for move in selected_piece.move(pieces):
        #     if move == (pieces[4].x, pieces[4].y):
        #         in_check_p1=True
        #     elif move == (pieces[28].x, pieces[28].y):
        #         in_check_p2=True

        captured_piece = next((p for p in pieces if p.x == col and p.y == row and p != selected_piece), None)
        if captured_piece:
            pieces.remove(captured_piece)
            #TODO: Move piece to sideobard
        if current_turn=='white':
            pw.set_turn(False)
            pb.set_turn(True)
            return 'black'
        else:
            pw.set_turn(True)
            pb.set_turn(False)
            return 'white'
    else:
        selected_piece.x, selected_piece.y = original_pos

    
    return current_turn

def draw_selected_piece_effect(WIN,selected_piece,original_mouse_pos,available_moves):
    mousex,mousey=pygame.mouse.get_pos()
    offsetx=mousex-original_mouse_pos[0]
    offsety=mousey-original_mouse_pos[1]
    for move in available_moves:
        pygame.draw.circle(WIN,(0,0,255),(move[0]*square_size+square_size//2,move[1]*square_size+square_size//2),12)
    # selected_piece.image=pygame.transform.scale(selected_piece.image, (selected_piece.scaled_width + 10,selected_piece.scaled_height + 10))
    # dx=(square_size-selected_piece.image.get_width())//2
    # dy=(square_size-selected_piece.image.get_height())//2
    # WIN.blit(selected_piece.image,(selected_piece.x*square_size+dx,selected_piece.y*square_size+dy))


    #calculate new position of selected_piece
    piecex,piecey=(selected_piece.x*square_size,selected_piece.y*square_size)
    selected_piece.draw_at((piecex,piecey),WIN)

def activate(button, text):
    if button==text[4]: #castle p1
        pass
    elif button==text[6]: #castle p2
        pass
    elif button==text[8]: #in check p1
        pygame.draw.rect()

WIN=pygame.display.set_mode((screen_width,screen_height))

def main():
    board=Board()
    pw = Player('white')
    pb = Player('black')
    current_turn= 'white' if pw.turn else 'black'
    dragging=False
    available_moves=[]
    original_pos=None
    selected_piece=None
    total_moves=1
    temp_total_moves=0
    while total_moves>0:
        #check for stalemate
        # for piece in pieces:
        #     temp_total_moves=len(piece.move(pieces))
        #     in_check_p1 = True 
        #     # if (pieces[4].x,pieces[4].y) in piece.move(pieces) or (pieces[60].x,pieces[60].y) in piece.move(pieces):
        #     #     pass
        # if temp_total_moves==0:
        #     total_moves=0
        
        # for piece in pieces:
        #     for move in piece.move():
        #         if move == (pieces[4][0],pieces[4][1]) or move == pieces[]:
        in_check_pb = is_in_check('black', pieces)
        in_check_pw = is_in_check('white', pieces)
        WIN.fill(WHITE)
        # blit buttons
        #TODO: if in check, only allow moves that block the check
        for i in range(0,len(text)-4,2):
            if i>3:
                pygame.draw.rect(WIN, OFFWHITE, (text[i+1][0]-6, text[i+1][1]-6, text[i+1][2]+12, text[i+1][3]+12))
                pygame.draw.rect(WIN, BLACK, (text[i+1][0]-6, text[i+1][1]-6, text[i+1][2]+12, text[i+1][3]+12), 2)
            WIN.blit(text[i],text[i+1])
        if not in_check_pb:
            pygame.draw.rect(WIN, OFFWHITE, (text[9][0]-6, text[9][1]-6, text[9][2]+12, text[9][3]+12))
            pygame.draw.rect(WIN, BLACK, (text[9][0]-6, text[9][1]-6, text[9][2]+12, text[9][3]+12), 2)
        if in_check_pb:
            pygame.draw.rect(WIN, (200,55,55), (text[9][0]-6, text[9][1]-6, text[9][2]+12, text[9][3]+12))
            pygame.draw.rect(WIN, BLACK, (text[9][0]-6, text[9][1]-6, text[9][2]+12, text[9][3]+12), 2)
        if not in_check_pw:
            pygame.draw.rect(WIN, OFFWHITE, (text[11][0]-6, text[11][1]-6, text[11][2]+12, text[11][3]+12))
            pygame.draw.rect(WIN, BLACK, (text[11][0]-6, text[11][1]-6, text[11][2]+12, text[11][3]+12), 2)
        if in_check_pw:
            pygame.draw.rect(WIN, (200,55,55), (text[11][0]-6, text[11][1]-6, text[11][2]+12, text[11][3]+12))
            pygame.draw.rect(WIN, BLACK, (text[11][0]-6, text[11][1]-6, text[11][2]+12, text[11][3]+12), 2)
        WIN.blit(text[8],text[9])
        WIN.blit(text[10],text[11])

        

        
        # pygame.draw.rect(WIN, BLACK, )
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                for button in range(1,len(text),2):
                    if text[button].collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                        activate(button, text)
                selected_piece,available_moves,original_pos,original_mouse_pos=handle_mouse_down(event,pieces,board, current_turn)
                dragging=selected_piece is not None
            if event.type==pygame.MOUSEBUTTONUP:
                current_turn = handle_mouse_up(event, dragging, selected_piece, original_pos, available_moves, pieces, pw, pb, current_turn)
                dragging = False
                print(current_turn)
            elif event.type==pygame.KEYDOWN:
                print(in_check_pb, in_check_pw)

        board.draw(WIN)
        for piece in pieces:
            piece.update(WIN)
        if selected_piece and dragging:
            draw_selected_piece_effect(WIN,piece,original_mouse_pos,available_moves)
        pygame.display.flip()


if __name__=='__main__':
    main()



