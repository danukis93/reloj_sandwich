jamon= 0
queso= 0
pan= 0

def setup():
    size(800, 400)

def draw():
    global jamon
    global queso
    global pan
    background(157, 131, 130)
    noStroke()
    fill(160, 212, 214)   
    square(jamon, 20, 55)
    if jamon > height:
       jamon = 0
    else:
       jamon = map(second(), 0, 59, 0, height)
    fill(242, 242, 147)
    ellipse(queso, height / 2, 55, 55)
    if queso > height:
       queso = 0
    else:
       queso = map(minute(), 0, 59, 0, height)
    fill(176, 160, 214)
    rect(pan, 280, 80, 50, 10)
    if pan > height:
       pan = 0
    else:
       pan = map(hour(), 0, 59, 0, height)
