def setup():
    size(500, 400)
    background(0)
    stroke(255)


def RGB2Luma(RGBvalue):
    R = (~ -RGBvalue & 0xff0000)/65535
    G = (~ -RGBvalue & 0x00ff00)/255
    B = (~ -RGBvalue & 0x0000ff)+1

    # using standard brightness calculation ITU BT.709
    return int(0.2126*R + 0.7152*G + 0.0722*B)

def draw():
    noFill()
    ellipse(width * 0.5, height * 0.5, 250, 100)
    
    loadPixels()
    
    print(~(pixels[0]))
    print( [ (~ -pixels[0]&0xff0000)/65535, (~ -pixels[0]&0x00ff00)/255, (~ -pixels[0]&0x0000ff)+1 ] )
    with open("demofile.txt", "a") as f:
        for i in range(0, len(pixels), width):
            
            f.write(str( RGB2Luma(pixels[i]) ))
            for j in range(1, width):
                f.write(", " + str( RGB2Luma(pixels[i+j]) ))
            f.write("\n")
    noLoop()
