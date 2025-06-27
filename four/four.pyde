def setup():
    size(500, 400)
    background(0)
    stroke(255)

def draw():
    noFill()
    ellipse(width * 0.5, height * 0.5, 250, 100)
    
    loadPixels()
    
    with open("demofile.txt", "a") as f:
        for i in range(len(pixels)):
            f.write(str(pixels[i]) + "\n")
    
    noLoop()
