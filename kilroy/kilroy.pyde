size(640, 480)
background(255)
fill(random(0, 255), random(0, 255), random(0, 255), 50)
noStroke()
circle(260, 240, 150)
fill(random(0, 255), random(0, 255), random(0, 255), 50)
circle(360, 240, 150)
fill(random(0, 255), random(0, 255), random(0, 255), 50)
strokeWeight(5)
stroke(0, 0, 0)
point(260, 240)
point(360, 240)
bezier(260, 275, 230, 400, 400, 400, 360, 275)
noFill()
bezier(260, 375, 230, 400, 400, 400, 360, 375)
