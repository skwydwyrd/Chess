# # data=[23,4,6,10]
# # data2=[12,23,5,9]


# # if any(value in data2 for value in data):
# #     print(True)

# class Queen(Piece):
#     def move(self,pieces):
#         can_move_to=[]
#         for i in range(1,8):
#             can_move_to.append((self.x+i,self.y))
#             can_move_to.append((self.x+i,self.y+i))
#             can_move_to.append((self.x-i,self.y))
#             can_move_to.append((self.x-i,self.y-i))
#             can_move_to.append((self.x,self.y+i))
#             can_move_to.append((self.x-i,self.y+i))
#             can_move_to.append((self.x,self.y-i))
#             can_move_to.append((self.x+i,self.y-i))
#         #FIXME:make it so that pieces can't move through each other
#         for piece in pieces:
#             for move in can_move_to:
#                 if piece.color== self.color and piece.x==move[0] and piece.y==move[1]:
#                     can_move_to.remove(move)
                
#         return can_move_to

# class Queen(Piece):
#     def move(self,pieces):
#         can_move_to=[]
        
#         directions=[(1,0),(1,1),(-1,0),(-1,-1),(0,1),(-1,1),(0,-1),(1,-1)]
#         for dr,dc in directions:
#             for i in range(1,8):
#                 x,y=self.x+i*dr,self.y+i*dc
#                 if not (0<=x<8 and 0<=y<8):
#                     break
#                 if any(piece.x==x and piece.y==y for piece in pieces):
#                     break
#                 can_move_to.append((x,y))


# next syntax:
# next(iterator,default)



lyst=(1,2,3,4,5,6)
words=['fruit','vegetables','dairy','meat']
result=None
for i in lyst:
    if i%2==0:
        print(f'{i} is even')
        result=i
    if not result:
        print('No even numbers')


first_even=next((x for x in lyst if x%2==0),None)
if first_even is not None:
    print(first_even)


first_big_word = next(
        (x for x in words if len(x) > 5),None
    )
if first_big_word is not None:
    print(first_big_word)

# class Animal:
#     def __init__(self):
#         self.type = 'mammal'

# class Dog(Animal):
#     def __init__(self):
#         self.name = 'tyler'

# class Cat(Animal):
#     def __init__(self):
#         self.name = 'skyler'


# animal = Cat()
# animal2 = Dog()
# if isinstance(animal,Cat):
#     print('animal is cat')
# else:
#     print('animal is dog')


# output: this is a cat/dog