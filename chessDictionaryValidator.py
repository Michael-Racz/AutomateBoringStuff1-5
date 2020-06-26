# 05/22/2020 Racz
# ABSWP CH5 
#
# Chess Dictionary Validator
# Does not check for more than one piece, or one king, besides pawns.


def isValidChessBoard(board_dict):
    #board will have one black king and one white king
    if 'bking' not in board_dict.values() or 'wking' not in board.dict_values():
        return False


    #each player can only have at most 16 pieces
    black_pieces = 0
    white_pieces = 0
    for piece in board_dict:
        if piece[0] == 'b':
            black_pieces +=1
        elif piece[0] == 'w':
            white_pieces +=1
    if black_pieces >= 17 or white_pieces >= 17:
        return False
    

    #each player can only have at most 8 pawns
    if sum(i == 'bpawn' for i in board_dict.values()) >= 9:
        return False
    if sum(i == 'wpawn' for i in board_dict.values()) >= 9:
        return False


    #Check for the piece in a valid location
    board_keys =list(board_dict)
    y=['1','2','3','4','5','6','7','8']
    #removes the first letter from the list
    board_y = [s[:1] for s in board_keys]
    if not all(elem in y for elem in board_y):
        return False
    
    x = ['a','b','c','d','e','f','g','h']
    board_x = [s[1:] for s in board_keys]
    if not all(elen in x for elen in board_x):
        return False


    #each piece must start with w or b
    for pieces in board_dict.values():
        if pieces[0] != 'b' and pieces[0] != 'w':
            return False


    #each piece must be on a valid space that 
    piece_names = ['pawn','knight','bishop','rook','queen','king']
    for names in board_dict.values():
        if names[1:] not in piece_names:
            return False
    
    # If they made it 
    return True