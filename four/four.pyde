def setup():
    size(500, 400)
    background(96, 20, 255)
    stroke(255)

def draw():
    noFill()
    ellipse(width * 0.5, height * 0.5, 250, 100)
    
    loadPixels()
    
    print(~(pixels[0]))
    print( [ (~ -pixels[0]&0xff0000)/65535, (~ -pixels[0]&0x00ff00)/255, (~ -pixels[0]&0x0000ff)+1 ] )
#    with open("demofile.txt", "a") as f:
#        for i in range(0, len(pixels), width):
    # using standard brightness calculation ITU BT.709
#            f.write(str(pixels[i]))
#            for j in range(1, width):
#                f.write(", " + str(pixels[i+j]))
#            f.write("\n")
    noLoop()
