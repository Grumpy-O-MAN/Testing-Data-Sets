#Hi peter, 
import time, math
def get_time():
    timenow = time.localtime()
    global Hour
    Hour = timenow.tm_hour
    global Mineut
    Mineut = timenow.tm_min
    global Secound
    Secound = timenow.tm_sec
ClockFace = []
column=[]
displayX=[]
displayY=[]
MinLength=6
SecLength=7
HrLength=4
#sets up the space
for y in range(15):
    column = [] # Create a new column.
    for x in range(15):
        column.append('  ') # Add two blank spaces
    ClockFace.append(column) # ClockFace is a list of column lists. 
def Display_Clock():
    for Y in range(15):
        print()
        for X in range(15):
            print(str(ClockFace[Y][X]),end='  ',)
        
def Clear_Clock():
    for Y in range(15):
       for X in range(15):
            ClockFace[Y][X]="  "  
get_time()
Clear_Clock()
while True:
    for i in range(HrLength):   
        xcord=(round(i*math.sin(math.radians((360*(Hour/12))))))+7
        ychord=(round(i*math.cos(math.radians((360*(Hour/12))))))+7
        ClockFace[-ychord][xcord]=Hour
    for i in range(MinLength):
        xcord=(round(i*math.sin(math.radians((360*(Mineut/60))))))+7
        ychord=(round(i*math.cos(math.radians((360*(Mineut/60))))))+7
        ClockFace[-ychord][xcord]=Mineut
    for i in range(SecLength):
            xcord=(round(i*math.sin(math.radians((360*(Secound/60))))))+7
            ychord=(round(i*math.cos(math.radians((360*(Secound/60))))))+7
            ClockFace[-ychord][xcord]=Secound
    Display_Clock()
    time.sleep(1)
    get_time()
    Clear_Clock()
                    
        
        
        
    
    