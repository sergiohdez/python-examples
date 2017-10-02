from shapes import Triangle, Rectangle, Oval

tr=Triangle() 
rc=Rectangle() 
ov=Oval()

for i in range(10):
  tr.randomise() 
  rc.randomise() 
  ov.randomise() 
  tr.draw() 
  rc.draw() 
  ov.draw()
