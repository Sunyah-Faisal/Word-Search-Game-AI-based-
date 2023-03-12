# Import modules
from tkinter import *
import random
import string

# splash screen
splash = Tk()
splash.geometry("800x500+350+150")

img = PhotoImage(file = "splash.png")

bg_label = Label(splash, image = img)
bg_label.place(x = 0, y = 0)

# Remove border of the splash Window
splash.overrideredirect(True)

                                                    # main window function
def playbtn():
    
    # destroy screen 2 window
    screen.destroy()

    
                        # generating table
    def wordGrid(wordlist):

        words = [wordlist[i].upper().replace("'",'').strip() \
        for i in range(len(wordlist)) ]

        grid_size = 12
        grid = [ [ '_' for _ in range(grid_size) ] for _ in range(grid_size) ]

        def print_grid():

            global puzzleComp
            puzzleComp = []

            for x in range(grid_size):
                puzzleComp.append(''.join(grid[x]))
##            print(puzzleComp)

            X0, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11 = puzzleComp[0], puzzleComp[1], puzzleComp[2], puzzleComp[3], puzzleComp[4], puzzleComp[5], puzzleComp[6], puzzleComp[7], puzzleComp[8], puzzleComp[9], puzzleComp[10], puzzleComp[11]
            font = ("Times New Roman",16, 'bold')
            
            L0A = Label(r, text = X0[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L0A.place(x = 50, y = 40)
            L0B = Label(r, text = X0[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L0B.place(x = 80, y = 40)
            L0C = Label(r, text = X0[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L0C.place(x = 110, y = 40)
            L0D = Label(r, text = X0[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L0D.place(x = 140, y = 40)
            L0E = Label(r, text = X0[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L0E.place(x = 170, y = 40)
            L0F = Label(r, text = X0[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L0F.place(x = 200, y = 40)
            L0G = Label(r, text = X0[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L0G.place(x = 230, y = 40)
            L0H = Label(r, text = X0[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L0H.place(x = 260, y = 40)
            L0I = Label(r, text = X0[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L0I.place(x = 290, y = 40)
            L0J = Label(r, text = X0[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L0J.place(x = 320, y = 40)
            L0K = Label(r, text = X0[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L0K.place(x = 350, y = 40)
            L0L = Label(r, text = X0[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L0L.place(x = 380, y = 40)

            L1A = Label(r, text = X1[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L1A.place(x = 50, y = 70)
            L1B = Label(r, text = X1[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L1B.place(x = 80, y = 70)
            L1C = Label(r, text = X1[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L1C.place(x = 110, y = 70)
            L1D = Label(r, text = X1[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L1D.place(x = 140, y = 70)
            L1E = Label(r, text = X1[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L1E.place(x = 170, y = 70)
            L1F = Label(r, text = X1[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L1F.place(x = 200, y = 70)
            L1G = Label(r, text = X1[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L1G.place(x = 230, y = 70)
            L1H = Label(r, text = X1[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L1H.place(x = 260, y = 70)
            L1I = Label(r, text = X1[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L1I.place(x = 290, y = 70)
            L1J = Label(r, text = X1[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L1J.place(x = 320, y = 70)
            L1K = Label(r, text = X1[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L1K.place(x = 350, y = 70)
            L1L = Label(r, text = X1[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L1L.place(x = 380, y = 70)

            L2A = Label(r, text = X2[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L2A.place(x = 50, y = 100)
            L2B = Label(r, text = X2[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L2B.place(x = 80, y = 100)
            L2C = Label(r, text = X2[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L2C.place(x = 110, y = 100)
            L2D = Label(r, text = X2[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L2D.place(x = 140, y = 100)
            L2E = Label(r, text = X2[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L2E.place(x = 170, y = 100)
            L2F = Label(r, text = X2[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L2F.place(x = 200, y = 100)
            L2G = Label(r, text = X2[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L2G.place(x = 230, y = 100)
            L2H = Label(r, text = X2[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L2H.place(x = 260, y = 100)
            L2I = Label(r, text = X2[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L2I.place(x = 290, y = 100)
            L2J = Label(r, text = X2[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L2J.place(x = 320, y = 100)
            L2K = Label(r, text = X2[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L2K.place(x = 350, y = 100)
            L2L = Label(r, text = X2[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L2L.place(x = 380, y = 100)

            L3A = Label(r, text = X3[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L3A.place(x = 50, y = 130)
            L3B = Label(r, text = X3[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L3B.place(x = 80, y = 130)
            L3C = Label(r, text = X3[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L3C.place(x = 110, y = 130)
            L3D = Label(r, text = X3[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L3D.place(x = 140, y = 130)
            L3E = Label(r, text = X3[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L3E.place(x = 170, y = 130)
            L3F = Label(r, text = X3[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L3F.place(x = 200, y = 130)
            L3G = Label(r, text = X3[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L3G.place(x = 230, y = 130)
            L3H = Label(r, text = X3[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L3H.place(x = 260, y = 130)
            L3I = Label(r, text = X3[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L3I.place(x = 290, y = 130)
            L3J = Label(r, text = X3[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L3J.place(x = 320, y = 130)
            L3K = Label(r, text = X3[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L3K.place(x = 350, y = 130)
            L3L = Label(r, text = X3[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L3L.place(x = 380, y = 130)

            L4A = Label(r, text = X4[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L4A.place(x = 50, y = 160)
            L4B = Label(r, text = X4[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L4B.place(x = 80, y = 160)
            L4C = Label(r, text = X4[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L4C.place(x = 110, y = 160)
            L4D = Label(r, text = X4[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L4D.place(x = 140, y = 160)
            L4E = Label(r, text = X4[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L4E.place(x = 170, y = 160)
            L4F = Label(r, text = X4[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L4F.place(x = 200, y = 160)
            L4G = Label(r, text = X4[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L4G.place(x = 230, y = 160)
            L4H = Label(r, text = X4[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L4H.place(x = 260, y = 160)
            L4I = Label(r, text = X4[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L4I.place(x = 290, y = 160)
            L4J = Label(r, text = X4[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L4J.place(x = 320, y = 160)
            L4K = Label(r, text = X4[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L4K.place(x = 350, y = 160)
            L4L = Label(r, text = X4[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L4L.place(x = 380, y = 160)

            L5A = Label(r, text = X5[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L5A.place(x = 50, y = 190)
            L5B = Label(r, text = X5[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L5B.place(x = 80, y = 190)
            L5C = Label(r, text = X5[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L5C.place(x = 110, y = 190)
            L5D = Label(r, text = X5[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L5D.place(x = 140, y = 190)
            L5E = Label(r, text = X5[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L5E.place(x = 170, y = 190)
            L5F = Label(r, text = X5[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L5F.place(x = 200, y = 190)
            L5G = Label(r, text = X5[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L5G.place(x = 230, y = 190)
            L5H = Label(r, text = X5[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L5H.place(x = 260, y = 190)
            L5I = Label(r, text = X5[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L5I.place(x = 290, y = 190)
            L5J = Label(r, text = X5[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L5J.place(x = 320, y = 190)
            L5K = Label(r, text = X5[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L5K.place(x = 350, y = 190)
            L5L = Label(r, text = X5[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L5L.place(x = 380, y = 190)

            L6A = Label(r, text = X6[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L6A.place(x = 50, y = 220)
            L6B = Label(r, text = X6[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L6B.place(x = 80, y = 220)
            L6C = Label(r, text = X6[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L6C.place(x = 110, y = 220)
            L6D = Label(r, text = X6[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L6D.place(x = 140, y = 220)
            L6E = Label(r, text = X6[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L6E.place(x = 170, y = 220)
            L6F = Label(r, text = X6[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L6F.place(x = 200, y = 220)
            L6G = Label(r, text = X6[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L6G.place(x = 230, y = 220)
            L6H = Label(r, text = X6[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L6H.place(x = 260, y = 220)
            L6I = Label(r, text = X6[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L6I.place(x = 290, y = 220)
            L6J = Label(r, text = X6[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L6J.place(x = 320, y = 220)
            L6K = Label(r, text = X6[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L6K.place(x = 350, y = 220)
            L6L = Label(r, text = X6[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L6L.place(x = 380, y = 220)

            L7A = Label(r, text = X7[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L7A.place(x = 50, y = 250)
            L7B = Label(r, text = X7[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L7B.place(x = 80, y = 250)
            L7C = Label(r, text = X7[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L7C.place(x = 110, y = 250)
            L7D = Label(r, text = X7[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L7D.place(x = 140, y = 250)
            L7E = Label(r, text = X7[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L7E.place(x = 170, y = 250)
            L7F = Label(r, text = X7[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L7F.place(x = 200, y = 250)
            L7G = Label(r, text = X7[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L7G.place(x = 230, y = 250)
            L7H = Label(r, text = X7[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L7H.place(x = 260, y = 250)
            L7I = Label(r, text = X7[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L7I.place(x = 290, y = 250)
            L7J = Label(r, text = X7[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L7J.place(x = 320, y = 250)
            L7K = Label(r, text = X7[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L7K.place(x = 350, y = 250)
            L7L = Label(r, text = X7[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L7L.place(x = 380, y = 250)

            L8A = Label(r, text = X8[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L8A.place(x = 50, y = 280)
            L8B = Label(r, text = X8[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L8B.place(x = 80, y = 280)
            L8C = Label(r, text = X8[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L8C.place(x = 110, y = 280)
            L8D = Label(r, text = X8[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L8D.place(x = 140, y = 280)
            L8E = Label(r, text = X8[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L8E.place(x = 170, y = 280)
            L8F = Label(r, text = X8[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L8F.place(x = 200, y = 280)
            L8G = Label(r, text = X8[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L8G.place(x = 230, y = 280)
            L8H = Label(r, text = X8[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L8H.place(x = 260, y = 280)
            L8I = Label(r, text = X8[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L8I.place(x = 290, y = 280)
            L8J = Label(r, text = X8[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L8J.place(x = 320, y = 280)
            L8K = Label(r, text = X8[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L8K.place(x = 350, y = 280)
            L8L = Label(r, text = X8[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L8L.place(x = 380, y = 280)

            L9A = Label(r, text = X9[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L9A.place(x = 50, y = 310)
            L9B = Label(r, text = X9[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L9B.place(x = 80, y = 310)
            L9C = Label(r, text = X9[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L9C.place(x = 110, y = 310)
            L9D = Label(r, text = X9[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L9D.place(x = 140, y = 310)
            L9E = Label(r, text = X9[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L9E.place(x = 170, y = 310)
            L9F = Label(r, text = X9[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L9F.place(x = 200, y = 310)
            L9G = Label(r, text = X9[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L9G.place(x = 230, y = 310)
            L9H = Label(r, text = X9[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L9H.place(x = 260, y = 310)
            L9I = Label(r, text = X9[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L9I.place(x = 290, y = 310)
            L9J = Label(r, text = X9[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L9J.place(x = 320, y = 310)
            L9K = Label(r, text = X9[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L9K.place(x = 350, y = 310)
            L9L = Label(r, text = X9[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L9L.place(x = 380, y = 310)

            L10A = Label(r, text = X10[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L10A.place(x = 50, y = 340)
            L10B = Label(r, text = X10[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L10B.place(x = 80, y = 340)
            L10C = Label(r, text = X10[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L10C.place(x = 110, y = 340)
            L10D = Label(r, text = X10[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L10D.place(x = 140, y = 340)
            L10E = Label(r, text = X10[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L10E.place(x = 170, y = 340)
            L10F = Label(r, text = X10[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L10F.place(x = 200, y = 340)
            L10G = Label(r, text = X10[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L10G.place(x = 230, y = 340)
            L10H = Label(r, text = X10[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L10H.place(x = 260, y = 340)
            L10I = Label(r, text = X10[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L10I.place(x = 290, y = 340)
            L10J = Label(r, text = X10[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L10J.place(x = 320, y = 340)
            L10K = Label(r, text = X10[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L10K.place(x = 350, y = 340)
            L10L = Label(r, text = X10[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L10L.place(x = 380, y = 340)

            L11A = Label(r, text = X11[0], font = font, bg = "#880e4f", fg = "#fafafa")
            L11A.place(x = 50, y = 370)
            L11B = Label(r, text = X11[1], font = font, bg = "#880e4f", fg = "#fafafa")
            L11B.place(x = 80, y = 370)
            L11C = Label(r, text = X11[2], font = font, bg = "#880e4f", fg = "#fafafa")
            L11C.place(x = 110, y = 370)
            L11D = Label(r, text = X11[3], font = font, bg = "#880e4f", fg = "#fafafa")
            L11D.place(x = 140, y = 370)
            L11E = Label(r, text = X11[4], font = font, bg = "#880e4f", fg = "#fafafa")
            L11E.place(x = 170, y = 370)
            L11F = Label(r, text = X11[5], font = font, bg = "#880e4f", fg = "#fafafa")
            L11F.place(x = 200, y = 370)
            L11G = Label(r, text = X11[6], font = font, bg = "#880e4f", fg = "#fafafa")
            L11G.place(x = 230, y = 370)
            L11H = Label(r, text = X11[7], font = font, bg = "#880e4f", fg = "#fafafa")
            L11H.place(x = 260, y = 370)
            L11I = Label(r, text = X11[8], font = font, bg = "#880e4f", fg = "#fafafa")
            L11I.place(x = 290, y = 370)
            L11J = Label(r, text = X11[9], font = font, bg = "#880e4f", fg = "#fafafa")
            L11J.place(x = 320, y = 370)
            L11K = Label(r, text = X11[10], font = font, bg = "#880e4f", fg = "#fafafa")
            L11K.place(x = 350, y = 370)
            L11L = Label(r, text = X11[11], font = font, bg = "#880e4f", fg = "#fafafa")
            L11L.place(x = 380, y = 370)

            global labelList
            labelList = [[L0A, L0B, L0C, L0D, L0E, L0F, L0G, L0H, L0I, L0J, L0K, L0L],
                         [L1A, L1B, L1C, L1D, L1E, L1F, L1G, L1H, L1I, L1J, L1K, L1L],
                         [L2A, L2B, L2C, L2D, L2E, L2F, L2G, L2H, L2I, L2J, L2K, L2L],
                         [L3A, L3B, L3C, L3D, L3E, L3F, L3G, L3H, L3I, L3J, L3K, L3L],
                         [L4A, L4B, L4C, L4D, L4E, L4F, L4G, L4H, L4I, L4J, L4K, L4L],
                         [L5A, L5B, L5C, L5D, L5E, L5F, L5G, L5H, L5I, L5J, L5K, L5L],
                         [L6A, L6B, L6C, L6D, L6E, L6F, L6G, L6H, L6I, L6J, L6K, L6L],
                         [L7A, L7B, L7C, L7D, L7E, L7F, L7G, L7H, L7I, L7J, L7K, L7L],
                         [L8A, L8B, L8C, L8D, L8E, L8F, L8G, L8H, L8I, L8J, L8K, L8L],
                         [L9A, L9B, L9C, L9D, L9E, L9F, L9G, L9H, L9I, L9J, L9K, L9L],
                         [L10A, L10B, L10C, L10D, L10E, L10F, L10G, L10H, L10I, L10J, L10K, L10L],
                         [L11A, L11B, L11C, L11D, L11E, L11F, L11G, L11H, L11I, L11J, L11K, L11L]]

        orientations = ['leftright', 'updown', 'diagonaldownleft', 'diagonaldownright' ]

        for word in words:
            word_lenght = len(word)

            placed = False
            while not placed:

                orientation = random.choice(orientations)

                if orientation == 'updown':
                    x_step = 1
                    y_step = 0
                if orientation == 'leftright':
                    x_step = 0
                    y_step = 1
                if orientation == 'diagonaldownright':
                    x_step = 1
                    y_step = 1
                if orientation == 'diagonaldownleft':
                    x_step = 1
                    y_step = -1

                x_position = random.randint(0, grid_size-1)
                y_position = random.randint(0, grid_size-1)

                ending_x = x_position + word_lenght*x_step
                ending_y = y_position + word_lenght*y_step

                if ending_x < 0 or ending_x >= grid_size: continue
                if ending_y < 0 or ending_y >= grid_size: continue

                failed = False

                for i in range(word_lenght):
                    character = word[i]
                    
                    new_position_x = x_position + i*x_step
                    new_position_y = y_position + i*y_step

                    character_at_new_position = grid[new_position_x][new_position_y]
                    if character_at_new_position != '_':
                        if character_at_new_position == character:
                            continue
                        else:
                            failed = True
                            break
                
                if failed:
                    continue
                else:
                    for i in range(word_lenght):
                        character = word[i]

                        new_position_x = x_position + i*x_step
                        new_position_y = y_position + i*y_step

                        grid[new_position_x][new_position_y] = character

                    placed = True

        for x in range(grid_size):
            for y in range(grid_size):
                if ( grid[x][y] == '_'):
                    grid[x][y] = random.choice(string.ascii_uppercase)

        print_grid()
        
                        # validating inputs
    def checkInputs(List):
        num = 0
        length = 0
        for i in List:
            if not i.isalpha():
                num+=1
            if len(i)<3:
                length+=1

        if '' not in List:                      # checking for empty inputs
            if num == 0:                        # checking for spaces, numeric and special characters
                if length == 0:                 # checking for less than 3 word length
                    emptyInput.grid_forget()
                    alphabet.place_forget()
                    minlength.place_forget()
                    tablebtn['state'] = DISABLED
                    word1['state'] = DISABLED
                    word2['state'] = DISABLED
                    word3['state'] = DISABLED
                    word4['state'] = DISABLED
                    word5['state'] = DISABLED
                    word6['state'] = DISABLED
                    word7['state'] = DISABLED
                    global finalList
                    finalList = [List[0].upper(), List[1].upper(), List[2].upper(), List[3].upper(), List[4].upper(), List[5].upper(), List[6].upper()]
                    wordGrid(List)
                else:
                    minlength.place(x = 15, y = 390)
            else:
                alphabet.place(x = 40, y = 390)
        else:
            emptyInput.grid(row = 9 , column = 1, padx = 50, pady = 10)

    def word_list():
        input1 = word1.get()
        input2 = word2.get()
        input3 = word3.get()
        input4 = word4.get()
        input5 = word5.get()
        input6 = word6.get()
        input7 = word7.get()
        Allwords = [input1, input2, input3, input4, input5, input6, input7]
        checkInputs(Allwords)
                        # searching algorithm
    def find_leftright(worditem, puzzle, row, col):
        start = [row, col]
        temp = ''
        indexFound = []
        for i in range(1, len(worditem)):
            if col<len(puzzle[0])-1:
                if worditem[i] == puzzle[row][col+1]:
                    temp = temp+puzzle[row][col+1]
                    indexFound.append([row, col+1])
                    col+=1
                    if len(temp) == len(worditem)-1 and temp == worditem[1:]:
                        found = True
                        break
                    else:
                        found = False
                        continue
                else:
                    found = False
            else:
                found = False
        if found:
            indexFound.insert(0, start)
            return indexFound

    def find_updown(worditem, puzzle, row, col):
        start = [row, col]
        temp = ''
        indexFound = []
        for i in range(1, len(worditem)):
            if row<len(puzzle[0])-1:
                if worditem[i] == puzzle[row+1][col]:
                    temp = temp+puzzle[row+1][col]
                    indexFound.append([row+1, col])
                    row+=1
                    if len(temp) == len(worditem)-1 and temp == worditem[1:]:
                        found = True
                        break
                    else:
                        found = False
                        continue
                else:
                    found = False
            else:
                found = False
        if found:
            indexFound.insert(0, start)
            return indexFound
    

    def find_diagonaldownR(worditem, puzzle, row, col):    
        start = [row, col]
        temp = ''
        indexFound = []
        for i in range(1, len(worditem)):
            if row<len(puzzle[0])-1 and col<len(puzzle[0])-1:
                if worditem[i] == puzzle[row+1][col+1]:
                    temp = temp+puzzle[row+1][col+1]
                    indexFound.append([row+1, col+1])
                    row+=1
                    col+=1
                    if len(temp) == len(worditem)-1 and temp == worditem[1:]:
                        found = True
                        break
                    else:
                        found = False
                        continue
                else:
                    found = False
            else:
                found = False
        if found:
            indexFound.insert(0, start)
            return indexFound

    def find_diagonaldownL(worditem, puzzle, row, col):
        start = [row, col]
        temp = ''
        indexFound = []
        for i in range(1, len(worditem)):
            if row<len(puzzle[0])-1 and col!=0:
                if worditem[i] == puzzle[row+1][col-1]:
                    temp = temp+puzzle[row+1][col-1]
                    indexFound.append([row+1, col-1])
                    row+=1
                    col-=1
                    if len(temp) == len(worditem)-1 and temp == worditem[1:]:
                        found = True
                        break
                    else:
                        found = False
                        continue
                else:
                    found = False
            else:
                found = False
        if found:
            indexFound.insert(0, start)
            return indexFound

    def search_order(worditem, puzzle, row, col):
        leftright = find_leftright(worditem, puzzle, row, col)
        if leftright == None:
            updown = find_updown(worditem, puzzle, row, col)
            if updown == None:
                diagonaldownR = find_diagonaldownR(worditem, puzzle, row, col)
                if diagonaldownR == None:
                    diagonaldownL = find_diagonaldownL(worditem, puzzle, row, col)
                    if diagonaldownL == None:
                        return None
                    else:
                        return diagonaldownL
                else:
                    return diagonaldownR
            else:
                return updown
        else:
            return leftright

    def find():
        found = False
        for word in finalList:
            for i in range(len(puzzleComp)):
                for j in range(len(puzzleComp[0])):
                    if word[0] == puzzleComp[i][j]:
                        a = search_order(word, puzzleComp, i, j)
                        if a == None:
                            found = False
                            continue
                        else:
                            found = True
                            break
                    else:
                        continue
                if found:
##                    print(word, a)
                    found = False
                    for s in range(len(a)):
                        first = a[s][0]
                        second = a[s][1]
##                        print(labelList[first][second])
                        labelList[first][second].config(bg = 'black')
                        
                    break
                else:
                    continue

                                                        # main window
    r = Tk()
    r.title('Word Search 12x12')
    r.geometry('800x500+350+150')
    r.resizable(0,0)
    r.config(bg = "#880e4f")

                                                        # input words frame
    wordsInput = LabelFrame(r , height = 500, width = 330, bg = "#76ff03")
    wordsInput.pack(side='right')
    wordsInput.grid_propagate(False)

                                                        # error messages for inputs
    emptyInput = Label(wordsInput, text = 'Please fill all entries first', font = ("Times New Roman",16), bg = "#76ff03")               # for empty inputs
    alphabet = Label(wordsInput, text = 'Only alphabets can be entered', font = ("Times New Roman",16), bg = "#76ff03")                 # for non-alphabetic characters
    minlength = Label(wordsInput, text = 'Words must have atleast 3 letters', font = ("Times New Roman",16), bg = "#76ff03")            # for less than 3 wordlength

                                                        # restricting input size
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()

    max_len = 10

    def on_write1(*args):
            s1 = var1.get()
            if len(s1) > max_len:
                    var1.set(s1[:max_len])
    def on_write2(*args):
            s2 = var2.get()
            if len(s2) > max_len:
                    var2.set(s2[:max_len])
    def on_write3(*args):
            s3 = var3.get()
            if len(s3) > max_len:
                    var3.set(s3[:max_len])
    def on_write4(*args):
            s4 = var4.get()
            if len(s4) > max_len:
                    var4.set(s4[:max_len])
    def on_write5(*args):
            s5 = var5.get()
            if len(s5) > max_len:
                    var5.set(s5[:max_len])
    def on_write6(*args):
            s6 = var6.get()
            if len(s6) > max_len:
                    var6.set(s6[:max_len])
    def on_write7(*args):
            s7 = var7.get()
            if len(s7) > max_len:
                    var7.set(s7[:max_len])

    var1.trace_variable("w", on_write1)
    var2.trace_variable("w", on_write2)
    var3.trace_variable("w", on_write3)
    var4.trace_variable("w", on_write4)
    var5.trace_variable("w", on_write5)
    var6.trace_variable("w", on_write6)
    var7.trace_variable("w", on_write7)

    message = Label(wordsInput, text = 'Enter your words:', font = ("Times New Roman",16), bg = "#76ff03")
    message.grid(row = 1, column = 1, padx = 50, pady = 10)

                                                            # inputs for words
    word1 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var1)
    word1.grid(row = 2, column = 1, padx = 50, pady = 10)

    word2 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var2)
    word2.grid(row = 3, column = 1, padx = 50, pady = 10)

    word3 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var3)
    word3.grid(row = 4, column = 1, padx = 50, pady = 10)

    word4 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var4)
    word4.grid(row = 5, column = 1, padx = 50, pady = 10)

    word5 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var5)
    word5.grid(row = 6, column = 1, padx = 50, pady = 10)

    word6 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var6)
    word6.grid(row = 7, column = 1, padx = 50, pady = 10)

    word7 = Entry(wordsInput, font = ("Times New Roman",16), textvariable = var7)
    word7.grid(row = 8, column = 1, padx = 50, pady = 10)

    tablebtn = Button(wordsInput, text = 'Generate table', font= ("Times New Roman",16), bg = "#ffc400", command = word_list)
    tablebtn.place(x = 100, y = 440)
    
    findWords = Button(r, text = 'Find words', font= ("Times New Roman",16), bg = "#00e5ff", command = find)
    findWords.place(x = 180, y = 440)

    r.mainloop()


                                                            # help button function

def helpbtn():
    Help['state'] = DISABLED
    about['state'] = NORMAL
    play.place(x = 570, y = 80)
    Help.place(x = 577, y = 210)
    about.place(x = 577, y = 340)

    # help messages

    global helpMsg1
    helpMsg1 = Label(screen, text = '1) You have to fill all entries.', font = ("Times New Roman",17, 'bold'), bg = 'red', fg = 'white')
    helpMsg1.grid(row = 1, column = 1, padx = 55, pady = 25)

    global helpMsg2
    helpMsg2 = Label(screen, text = '2) Word length must be minimum 3 and \n maximum 10.', font = ("Times New Roman",17, 'bold'), bg = 'red', fg = 'white')
    helpMsg2.grid(row = 2, column = 1, padx = 55, pady = 25)

    global helpMsg3
    helpMsg3 = Label(screen, text = '3) You must not enter any numbers, special \n characters or spaces.', font = ("Times New Roman", 17, 'bold'), bg = 'red', fg = 'white')
    helpMsg3.grid(row = 3, column = 1, padx = 55, pady = 25)

    global helpMsg4
    helpMsg4 = Label(screen, text = '4) If you are unable to generate table, \n please read the error messages displayed.', font = ("Times New Roman",17, 'bold'), bg = 'red', fg = 'white')
    helpMsg4.grid(row = 4, column = 1, padx = 55, pady = 25)

    global helpMsg5
    helpMsg5 = Label(screen, text = '5) If you still find difficulty, it might be \n due to spaces at the end of words', font = ("Times New Roman",17, 'bold'), bg = 'red', fg = 'white')
    helpMsg5.grid(row = 5, column = 1, padx = 55, pady = 25)

                                                            # about button function
def aboutbtn():
    about['state'] = DISABLED
    helpMsg1.grid_forget()
    helpMsg2.grid_forget()
    helpMsg3.grid_forget()
    helpMsg4.grid_forget()
    helpMsg5.grid_forget()

    abt = Label(screen, text = 'From the NED University\'s Department of \nComputer System Engineering, Aleena Yameen,\n Aira Farman, and Sunyah Faisal designed the\n WORD SEARCH. It is the outcome of endless\n hours of effort by the three students who were\n committed to finishing this project. After\n reviewing the requisite Artificial Intelligence\n information, we developed this project.',
                font = ("Times New Roman",17, 'bold'), bg = 'red', fg = 'white')
    abt.pack(side = 'left', padx = 40, pady = 30)
                                                                # second screen

def screen2():
    
    # destroy splash window
    splash.destroy()

    global screen
    screen = Tk()
    screen.title('Word Search 12x12')
    screen.geometry("800x500+350+150")
    screen.resizable(0,0)

    img = PhotoImage(file = "screen2.png")

    bg_label = Label(screen, image = img)
    bg_label.place(x = 0, y = 0)

    global play
    play = Button(screen, text = 'Play Now!' ,font= ("Times New Roman",16), bg = "#00e5ff", command = playbtn)
    play.place(x = 350, y = 80)

    global Help
    Help = Button(screen, text = 'Get Help', font= ("Times New Roman",16), bg = "#00e5ff", command = helpbtn)
    Help.place(x = 357, y = 210)

    global about
    about = Button(screen, text = 'About us', font= ("Times New Roman",16), bg = "#00e5ff", command = aboutbtn)
    about.place(x = 357, y = 340)

    screen.mainloop()


# splash interval
splash.after(3000, screen2)

# Execute tkinter
mainloop()



