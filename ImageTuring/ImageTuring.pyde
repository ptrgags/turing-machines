ROWS = 50
COLS = 50
COLORS = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]
SPEED = 10 #instructions per frame


grid = [[0 for col in range(COLS)] for j in range(ROWS)]
cur = PVector(0, 0)

'''
PROGRAM = [
    ["if", 0],
    ["jump", 4],
    ["down"],
    ["jump", 0],
    ["set", 1],
    ["right"],
    #["down"],
    ["jump", 0]
]
'''



PROGRAM = [
    ["if", 0],
    ["jump", 13],
    ["jump", 3],
    ["set", 2],
    ["up"],
    ["right"],
    ["up"],
    ["right"],
    ["noop"],
    ["noop"],
    ["noop"],
    ["noop"],
    ["jump", 0],
    ["set", 1],
    ["right"],
    ["right"],
    ["down"],
    ["noop"],
    ["noop"],
    ["noop"],
    ["noop"],
    ["noop"],
    ["jump", 0]
]
            

programCursor = 0;

def setup():
    size(500, 500)
    
def draw():
    global grid, programCursor
    
    for i in range(SPEED):
        programCursor = processStep(PROGRAM, programCursor)
    
    background(255)
    
    noStroke()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            fill(*COLORS[val])
            rect(x * 10, y * 10, 10, 10)
            
    stroke(0, 255, 255)
    noFill()
    rect(cur.x * 10, cur.y * 10, 10, 10)

def processStep(prgm, prgmCur):
    global cur, grid
    instruction = prgm[prgmCur]
    opcode = instruction[0]
    if opcode == "right":
        cur.x += 1
        if cur.x == COLS:
            cur.x = 0
    elif opcode == "left":
        cur.x -= 1
        if cur.x == -1:
            cur.x = COLS - 1
    elif opcode == "up":
        cur.y -= 1
        if cur.y == -1:
            cur.y = ROWS - 1
    elif opcode == "down":
        cur.y += 1
        if cur.y == ROWS:
            cur.y = 0
    elif opcode == "set":
        grid[int(cur.y)][int(cur.x)] = instruction[1]
    elif opcode == "jump":
        return instruction[1]
    elif opcode == "if":
        if grid[int(cur.y)][int(cur.x)] == instruction[1]:
            return prgmCur + 1
        else:
            return prgmCur + 2
    elif opcode == "noop":
        pass
    
    return prgmCur + 1
        
    
    
