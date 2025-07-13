# ---1.Define Cube Colors---
# we will use single letter characters for simplicity,correspondig to the colors of a rubix cube
#U(up)    -  white(W)
#D(Down)  -  Yellow(Y)
#F(Front) -  Green(G)
#B(Back)  -  Blue(B)
#L(Left)  - Orange(O)
#R(Right) - Red(R)

colors ={
  'W':'White',
  'Y':'Yellow',
  'G':'Green',
  'B':'Blue',
  'O':'Orange',
  'R':'Red'
}

#---2.Represent the Solved state ---
#We'll use a list of 6 faces.Each face is a 3*3 grid(list of 3 lists)>
#The order of faces is a commom convention:
#[0] = up(U)
#[1] = Front(F)
#[2] = Right (R)
#[3] = Back(B)
#[4] = Left(L)
#[5] = Down(D)

#Each 'cell' represents a sticker.In a solved state,all 9 stickers on a face are the same color.
#Example:Uface is al White 'W'
# W W W
# W W W
# W W W

def get_solved_cube():
Returns a representation of a cube solved 3*3 Rubix Cube.

  Cube =[
       #Up(U)  Face - White
       [['W', 'W' , 'W'],
        ['W', 'W' , 'W'],
        ['W', 'W' , 'W']],
  
      #Front(F) Face - Green
        [['G', 'G', 'G'],
         ['G', 'G', 'G'],
         ['G', 'G', 'G'],

      #Right(R)Face - Red 
         [['R', 'R', 'R'],
         ['R', 'R', 'R'],
         ['R', 'R', 'R']],

        # Back (Blue)
        [['B', 'B', 'B'],
         ['B', 'B', 'B'],
         ['B', 'B', 'B']],

        # Left (Orange)
        [['O', 'O', 'O'],
         ['O', 'O', 'O'],
         ['O', 'O', 'O']],

        # Down (Yellow)
        [['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y'],
         ['Y', 'Y', 'Y']]
    ]
    return cube
         
