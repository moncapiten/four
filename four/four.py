import py5



def setup():
    py5.size(500, 400)
    py5.smooth()
    py5.background(1) # DO NOT USE 0
    py5.stroke(255)
    py5.frame_rate(5)



def RGB2Luma(RGBvalue):
    R = (~ -RGBvalue & 0xff0000)/65535
    G = (~ -RGBvalue & 0x00ff00)/255
    B = (~ -RGBvalue & 0x0000ff)+1

    # using standard brightness calculation ITU BT.709
    return int(0.2126*R + 0.7152*G + 0.0722*B)

def save2file(filename, mode = "a"):
    py5.loadPixels()    
    with open("mario.txt", "w") as f:
        for i in range(0, len(py5.pixels), py5.width):

            f.write(str( RGB2Luma(py5.pixels[i]) ))
            for j in range(1, py5.width):
                f.write(", " + str( RGB2Luma(py5.pixels[i+j]) ))
            f.write("\n")

angle = 0
def draw():
    py5.background(1) # DO NOT USE 0
    py5.fill(1)

    global angle

    py5.translate(250, 220)
    py5.rotate(angle)
    py5.ellipse(-60,-90,100,100) #circle 2
    py5.ellipse(60,-90,100,100) #circle 3
    py5.ellipse(0, 0,150,150) #circle 1

 
    angle = angle + py5.PI/20
    if (angle >=2*py5.PI):
        angle = 0
#    noLoop()
    
    
    
    
    


py5.run_sketch()