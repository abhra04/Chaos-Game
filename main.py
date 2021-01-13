import random

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
count = 0
#(n,r) varies to give different shapes
print("Choose How you want to play:")
#1 - Custom Made Polygon
#2 - Regular Polygon(Predefined Size)
print("1 : if you want to have your own polygon")
print("2 : if you want to see a simple regular polygon")
choice = int(input())

if choice == 1:
    arr = []
    print("Size of the polygon")
    n = int(input())
    for _ in range(n):
        print("Enter Coordinates of the polygon:")
        x = int(input())
        y = int(input())
        arr.append([x,y])

    print("Enter initial Coordinates")
    x0 = int(input())
    y0 = int(input())
    print("Enter The Compression Ratio:")
    r = int(input())
    print("Number of Iterations:")
    i = int(input())
elif choice == 2:
    print("Enter the size of the regular Polygon:")
    n = int(input())
    print("Enter The Compression Ratio:")
    r = int(input())
    print("Number of Iterations:")
    i = int(input())
    if n == 3:
        arr = [[150,150],[200,150],[175,194]]
    if n == 4:
        arr = [ [150,150],[200,200],[150,200], [200,150]  ]

    if n == 5:
        arr = [ [150,150] , [200,150] , [250,200],[100,200],[175,250]  ]

    if n == 6:
        arr = [ [150,150] , [200,150],[100,200],[250,200],[150,250],[200,250]  ]

    x0 = 0
    y0 = 0 


print("Would you like to choose a background color?")
print("Press 1: Yes")
print("Press 2 :No")
wish = int(input())
if wish == 1:
    print("RGB Values in 255 Scale")
    print("Enter r value:")
    r2 = int(input())
    print("Emter g value:")
    g = int(input())
    print("Enter b value:")
    b = int(input())

    Window.clearcolor = (r2/255.00,g/255.0,b/255.0,1)
else:
    r2 = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    Window.clearcolor = (r2/255.00,g/255.0,b/255.0,1)




print("Would you like to choose color of your points:")
print("Press 1 : Yes")
print("Press 2: No")
x = int(input())
if x == 1:
    print("RGB Values seperated by a Space:")
    r1,g1,b1 = map(int,input().split(' '))
else:
    r1 = random.randint(0,255)
    g1 = random.randint(0,255)
    b1 = random.randint(0,255)


print("Select speed of the simulation:")
print("Press 1: Fast")
print("Press 2: Medium")
print("Press 3:Slow")
speed = int(input())
if speed == 1:
    call = 30
elif speed == 2:
    call = 10

else:
    call = 5




class ChaosGame(Widget):

    def Startgame(self,dt):
        global count,n,r,i
        count = count + 1
        print(count)
        if count>i:
            return False
        global arr,x0,y0
        global r1,g1,b1
        self.canvas.add(Color(rgb=(r1 / 255.0, g1 / 255.0, b1 / 255.0)))
        d = 4
        a = random.randint(0,n-1)
        x = arr[a][0]
        y = arr[a][1]

        x0 = (r*x+ x0)/r
        y0 =  (r*y + y0)/r
        self.canvas.add(Ellipse(pos=(x0,y0), size=(d, d)))
        
        

class ChaosApp(App):
    def build(self):
        global call
        game = ChaosGame()
        Clock.schedule_interval(game.Startgame,1/call)
        return game



ChaosApp().run()
