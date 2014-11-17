import serial
import time

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
    
    def isSpace(self):
        if (not(self.p1) and not(self.p2) and not(self.p3) and not(self.p4) and not(self.p5) and not (self.p6)):
            return True
        else:
            return False

class brailleConverter:
    cellList = []
    
    def __init__(self, str):
        
        #Split to words
        spl = str.split(" ")

        #for each word
        for i in range (0, len(spl)):
            #for each letter
            for j in range (0, len(spl[i])):
                currC = Cell()
                self.grade1Scan(currC, spl[i][j])
                self.cellList.append(currC)
            #add a space
            spaceC = Cell()
            self.cellList.append(spaceC)
            
            
    def getCellList(self):
        return self.cellList
            
    def grade1Scan(self, c, s):
        if (s == 'a' or s=='1'): 
            c.setPos1(1)
        elif (s == "b" or s =="2"):
            c.setPos1(1) 
            c.setPos3(1)
        elif (s == 'c' or s=='3'):
            c.setPos1(1)
            c.setPos2(1)
        elif (s == 'd' or s=='4'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos4(1)
        elif (s == 'e' or s=='5'):
            c.setPos1(1)
            c.setPos4(1)
        elif (s == 'f' or s=='6'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos3(1)
        elif (s == 'g' or s=='7'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos3(1)
            c.setPos4(1)
        elif (s == 'h' or s=='8'):
            c.setPos1(1)
            c.setPos3(1)
            c.setPos4(1)
        elif (s == 'i' or s=='9'):
            c.setPos2(1)
            c.setPos3(1)
        elif (s == 'j' or s=='0'):
            c.setPos2(1)
            c.setPos3(1)
            c.setPos4(1)
        elif (s == 'k'):
            c.setPos1(1)
            c.setPos5(1)
        elif (s == 'l'):
            c.setPos1(1)
            c.setPos3(1)
            c.setPos5(1)
        elif (s == 'm'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos5(1)
        elif (s == 'n'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == 'o'):
            c.setPos1(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == 'p'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos3(1)
            c.setPos5(1)
        elif (s == 'q'): 
            c.setPos1(1)
            c.setPos2(1)
            c.setPos3(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == 'r'): 
            c.setPos1(1)
            c.setPos3(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == 's'): 
            c.setPos2(1)
            c.setPos3(1)
            c.setPos5(1)
        elif (s == 't'): 
            c.setPos2(1)
            c.setPos3(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == 'u'):
            c.setPos1(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == 'v'):
            c.setPos1(1)
            c.setPos3(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == 'w'):
            c.setPos2(1)
            c.setPos3(1)
            c.setPos4(1)
            c.setPos6(1)
        elif (s == 'x'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == 'y'):
            c.setPos1(1)
            c.setPos2(1)
            c.setPos4(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == 'z'):
            c.setPos1(1)
            c.setPos4(1)
            c.setPos5(1)
            c.setPos6(1)
        #Symbols
        elif (s == ','):
            c.setPos3(1)
        elif (s == ';'):
            c.setPos3(1)
            c.setPos5(1)
        elif (s == ':'):
            c.setPos3(1)
            c.setPos4(1)
        elif (s == '.'):
            c.setPos3(1)
            c.setPos4(1)
            c.setPos6(1)
        elif (s == '!'):
            c.setPos3(1)
            c.setPos4(1)
            c.setPos5(1)
        elif (s == '('  or s == ')'):
            c.setPos3(1)
            c.setPos4(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == '?' or s == '\"'):
            c.setPos3(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == '*'):
            c.setPos4(1)
            c.setPos5(1)
        elif (s == '\"'):
            c.setPos4(1)
            c.setPos5(1)
            c.setPos6(1)
        elif (s == '\''):
            c.setPos5(1)
        elif (s == '-'):
            c.setPos5(1)
            c.setPos6(1)
        #Signals and Signs here if needed

                    
class printFormat:
    ROWSIZE = 8
    
    def __init__(self, cL):
        start = bytes("start", 'UTF-8')
        one = bytes("1", 'UTF-8')
        zero = bytes("0", 'UTF-8')
        tab = bytes("tab", 'UTF-8')
        down = bytes("down", 'UTF-8')
        row = bytes("row", 'UTF-8')
        done = bytes("done", 'UTF-8')
        
        ser = serial.Serial("COM3", 9600)
        counter = 0
        rows = int(len(cL)/self.ROWSIZE)
        remainder = len(cL) % self.ROWSIZE
        
        #for rows in cL
        print("=================================================================================")
        for i in range(0, rows):
            #for each cell row
            for j in range(0, 3):
                # reset the head all the way left
                ser.write(start)
                time.sleep(1)
                #
                
                #for each cell in the row
                for k in range(0, self.ROWSIZE):                        
                    #if first row
                    if (j == 0):
                        if(cL[counter+k].getPos1()):
                            print(".",  end="")
                            #print in slot 1
                            ser.write(one)
                            time.sleep(1)
                            #                            
                        else:
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                        if(cL[counter+k].getPos2()):
                            print(".",  end="")
                            ser.write(one)
                            time.sleep(1)
                        else:
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                        
                        
                    #if second row
                    elif(j == 1):
                        if(cL[counter+k].getPos3()):
                            print(".",  end="")
                            ser.write(one)
                            time.sleep(1)
                        else:
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                        if(cL[counter+k].getPos4()):
                            print(".",  end="")
                            ser.write(one)
                            time.sleep(1)
                        else:
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                        
                    #if third row
                    elif(j == 2):
                        if(cL[counter+k].getPos5()):
                            print(".",  end="")
                            ser.write(one)
                            time.sleep(1)
                        else:
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                        if(cL[counter+k].getPos6()):
                            print(".",  end="")
                            ser.write(one)
                            time.sleep(1)
                        else:                            
                            print(" ",  end="")
                            ser.write(zero)
                            time.sleep(1)
                            
                    #tab to the next cell
                    #tab step
                    ser.write(tab)
                    time.sleep(1)
                    #
                    print("\t",  end="")
                
                #down step
                ser.write(down)
                time.sleep(1)
                #
                print()
            
            counter+=self.ROWSIZE
            print("================================================================================")
            # drop a line step
            ser.write(row)
            time.sleep(1)
            #
            
            
        #For the remainder
        for i in range(0, 3):
            #reset the head to the far left
            ser.write(start)
            time.sleep(1)
            #
            for rem in range (0, remainder):
                # first cell row
                if (i == 0):
                    if(cL[counter+rem].getPos1()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:
                        print(" ",  end="")
                        ser.write(zero)
                        time.sleep(1)
                    if(cL[counter+rem].getPos2()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:                            
                        print(" ",  end="")
                        ser.write(zero)
                        time.sleep(1)
                
                # second cell row
                elif (i == 1):
                    if(cL[counter+rem].getPos3()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:
                        print(" ",  end="")
                        ser.write(zero)
                        time.sleep(1)
                    if(cL[counter+rem].getPos4()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:                            
                        print(" ",  end="")                     
                        ser.write(zero)
                        time.sleep(1)
                
                # third cell row
                elif (i == 2):
                    if(cL[counter+rem].getPos5()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:
                        print(" ",  end="")
                        ser.write(zero)
                        time.sleep(1)
                    if(cL[counter+rem].getPos6()):
                        print(".",  end="")
                        ser.write(one)
                        time.sleep(1)
                    else:                            
                        print(" ",  end="")
                        ser.write(zero)
                        time.sleep(1)
                # tab step
                ser.write(tab)
                time.sleep(1)
                #
                print("\t",  end="")
            # cell row step
            ser.write(down)
            time.sleep(1)
            #
            print()
        ser.write(done)
        ser.close()
 
class filePrint:
    
    def __init__(self, file):
        print(file)
        
        try:
            with open (file, "r") as myfile:
                str=myfile.read().replace('\n', '')
                
            str = str.lower()
    
            test = brailleConverter(str)
            printFormat(test.getCellList())                
        except:
            return None
            
        
        
#import sys                
#class printGUI():
    #response = input("Enter the text to print: ")
    #response = response.lower()
    #test = brailleConverter(response)
    #printFormat(test.getCellList())

#begin the interface everything
#printGUI()