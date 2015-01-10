import time
import textwrap

class Cell:    
    def __init__(self):
            self.p1 = False
            self.p2 = False
            self.p3 = False
            self.p4 = False
            self.p5 = False
            self.p6 = False
            
    def setPos1(self, b):
            if (self.p1):
                self.p1 = False
            else: 
                self.p1 = True    

    def setPos2(self, b):
            if (self.p2):
                self.p2 = False
            else: 
                self.p2 = True

    def setPos3(self, b):
            if (self.p3):
                self.p3 = False
            else: 
                self.p3 = True

    def setPos4(self, b):
            if (self.p4):
                self.p4 = False
            else: 
                self.p4 = True    
    
    def setPos5(self, b):
            if (self.p5):
                self.p5 = False
            else: 
                self.p5 = True            
    def setPos6(self, b):
            if (self.p6):
                self.p6 = False
            else: 
                self.p6 = True
                
    def getPos1(self):
        return self.p1
    def getPos2(self):
        return self.p2
    def getPos3(self):
        return self.p3
    def getPos4(self):
        return self.p4
    def getPos5(self):
        return self.p5
    def getPos6(self):
        return self.p6
    def list(self):
        return [[self.p1, self.p2], [self.p3, self.p4], [self.p5, self.p6]]



def grade1_convert(s):
    s = s.lower()
    cell = Cell()
    if (s == 'a' or s=='1'): 
        cell.setPos1(1)
    elif (s == "b" or s =="2"):
        cell.setPos1(1) 
        cell.setPos3(1)
    elif (s == 'c' or s=='3'):
        cell.setPos1(1)
        cell.setPos2(1)
    elif (s == 'd' or s=='4'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos4(1)
    elif (s == 'e' or s=='5'):
        cell.setPos1(1)
        cell.setPos4(1)
    elif (s == 'f' or s=='6'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos3(1)
    elif (s == 'g' or s=='7'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos4(1)
    elif (s == 'h' or s=='8'):
        cell.setPos1(1)
        cell.setPos3(1)
        cell.setPos4(1)
    elif (s == 'i' or s=='9'):
        cell.setPos2(1)
        cell.setPos3(1)
    elif (s == 'j' or s=='0'):
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos4(1)
    elif (s == 'k'):
        cell.setPos1(1)
        cell.setPos5(1)
    elif (s == 'l'):
        cell.setPos1(1)
        cell.setPos3(1)
        cell.setPos5(1)
    elif (s == 'm'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos5(1)
    elif (s == 'n'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == 'o'):
        cell.setPos1(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == 'p'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos5(1)
    elif (s == 'q'): 
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == 'r'): 
        cell.setPos1(1)
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == 's'): 
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos5(1)
    elif (s == 't'): 
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == 'u'):
        cell.setPos1(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == 'v'):
        cell.setPos1(1)
        cell.setPos3(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == 'w'):
        cell.setPos2(1)
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos6(1)
    elif (s == 'x'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == 'y'):
        cell.setPos1(1)
        cell.setPos2(1)
        cell.setPos4(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == 'z'):
        cell.setPos1(1)
        cell.setPos4(1)
        cell.setPos5(1)
        cell.setPos6(1)
    #Symbols
    elif (s == ','):
        cell.setPos3(1)
    elif (s == ';'):
        cell.setPos3(1)
        cell.setPos5(1)
    elif (s == ':'):
        cell.setPos3(1)
        cell.setPos4(1)
    elif (s == '.'):
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos6(1)
    elif (s == '!'):
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == '('  or s == ')'):
        cell.setPos3(1)
        cell.setPos4(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == '?' or s == '\"'):
        cell.setPos3(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == '*'):
        cell.setPos4(1)
        cell.setPos5(1)
    elif (s == '\"'):
        cell.setPos4(1)
        cell.setPos5(1)
        cell.setPos6(1)
    elif (s == '\''):
        cell.setPos5(1)
    elif (s == '-'):
        cell.setPos5(1)
        cell.setPos6(1)
    return cell


#left = b'1'
right = b'2'
up = b'4'
down = b'3'
dot = b'5'
right_in_cell = b'6'
down_in_cell = b'7'
left_in_cell = b'8'
done = b'1'
rollout = b'r'
rollin = b'g'

dots_per_line = 40;
move_right = 0
move_right2 = 0
from serial import Serial
buffer = []

if __name__ == "__main__":
    text = input("text = ")
    #text = "hello"
    lines = textwrap.wrap(text, int(dots_per_line/2))

    for line in lines:
        print("line = ", line)
        cells = [grade1_convert(x) for x in line] # current line of cells

        for level in range(3): # each row of the cells
            for cell in cells: # go through cells one by one
                cell = cell.list()

                if cell[level][0]:
                    print(".", end="")
                    buffer.append(dot)
                else:
                    print(" ", end="")

                buffer.append(right_in_cell)
                print(" ", end="")

                if cell[level][1]:
                    print(".", end="")
                    buffer.append(dot)
                else:
                    print(" ", end="")

                buffer.append(right)
                print(" ", end="")

            
            buffer.append(done)
            #for x in range(len(cells)):
                #buffer.append(left)
                #buffer.append(left_in_cell)

            buffer.append(down_in_cell)
            print(" ")
        buffer.append(down)
        print(" ")
    buffer.append(rollout)


print(buffer)
serial = Serial("/dev/ttyACM0", 9600)
time.sleep(3)
input("Start...")
serial.write(rollin)
time.sleep(3)
for x in buffer:
    print("Sending: ", x)
    serial.write(x)
    time.sleep(0.75)






serial.close()