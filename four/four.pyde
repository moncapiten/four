def setup():
    size(500, 400)
    smooth()
    background(1) # DO NOT USE 0
    stroke(255)
    
    angle = 0


def RGB2Luma(RGBvalue):
    R = (~ -RGBvalue & 0xff0000)/65535
    G = (~ -RGBvalue & 0x00ff00)/255
    B = (~ -RGBvalue & 0x0000ff)+1

    # using standard brightness calculation ITU BT.709
    return int(0.2126*R + 0.7152*G + 0.0722*B)

def save2file(filename, mode = "a"):
    loadPixels()    
    with open("mario.txt", "w") as f:
        for i in range(0, len(pixels), width):
            
            f.write(str( RGB2Luma(pixels[i]) ))
            for j in range(1, width):
                f.write(", " + str( RGB2Luma(pixels[i+j]) ))
            f.write("\n")



def draw():
    
    fill(1)
    
    translate(250, 220);
    rotate(angle)
    ellipse(-60,-90,100,100) #circle 2
    ellipse(60,-90,100,100) #circle 3
    ellipse(0, 0,150,150) #circle 1
 
    angle = angle + 0.1
#    angle = angle + PI/4
#    if (angle >=2*PI):
#        angle = 0
    


    
    
            
#    noLoop()
    
    
    
    
    
