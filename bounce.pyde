ball_y = 100
ball_x = 100
ball2_y = 70 
ball2_x = 70
y_speed = 4
x_speed = 4
def setup(): # runs once 
    size(500,500)
    
def draw(): # runs multiple times (loops)
    global ball_y
    global ball2_y
    global ball_x 
    global ball2_x 
    global y_speed
    global x_speed 
    
    
    background(200, 200, 200)
    ellipse(ball_x, ball_y, 100, 100)
    ellipse(ball2_x, ball2_y, 100, 100)
    line(0, 400, 500, 400)
    
    ball_y = ball_y + y_speed 
    ball_x = ball_x + x_speed
    
    if ball_y > 350: 
        print("BOUNCE")
        y_speed=-y_speed
        
    if ball_y < 50: 
        y_speed = 4
        
    if ball_x > 450:
        x_speed = -x_speed
        
    if ball_x < 50 :
        x_speed = 4
 
    ball2_y = ball2_y + y_speed 
    ball2_x = ball2_x + x_speed   
        
    if ball2_y > 350: 
        print("BOUNCE")
        y_speed=-y_speed
        
    if ball2_y < 50: 
        y_speed = 4
        
    if ball2_x > 450:
        x_speed = -x_speed
        
    if ball2_x < 50 :
        x_speed = 4
        
        

        
    
    
        
    
    
        
