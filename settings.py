import pygame

spritesheet = pygame.image.load('chess_pieces.png')
sheet_width, sheet_height = spritesheet.get_size()
screen_height=800
screen_width=1300
piece_width = sheet_width // 6
piece_height = sheet_height // 2
board_size=8
square_size=100

WHITE=(255,255,255)
BLACK=(0,0,0)
OFFWHITE=(235, 235, 255)

def load_pieces(spriesheet):
    pieces_dict={}
    labels=['king','queen','bishop','knight','rook','pawn']
	
    for i,label in enumerate(labels):
        pieces_dict[f'white_{label}']=spritesheet.subsurface(i*piece_width,0,piece_width,piece_height)
        pieces_dict[f'black_{label}']=spritesheet.subsurface(i*piece_width,piece_height,piece_width,piece_height)
    return pieces_dict

def update_selected_piece(pieces,selected_piece, available_moves=[]):
    mousex,mousey=pygame.mouse.get_pos()
    col,row=(mousex//square_size,mousey//square_size)
    if selected_piece is None:
        for i in pieces:
            if i.x==col and i.y==row:
                selected_piece=i
                available_moves=selected_piece.move()

pieces_data=load_pieces(spritesheet)
pieces_layout=[
    ('rook','knight','bishop','queen','king','bishop','knight','rook'),
    ('pawn',) * 8,
    (),
    (),
    (),
    (),
    ('pawn',) * 8,
    ('rook','knight','bishop','queen','king','bishop','knight','rook')
]