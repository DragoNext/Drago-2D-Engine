#Breshenham line algorithm
if __name__ == '__main__':
	import math

def naiveline(x1,y1,x2,y2):
    points = []
    rise = y2-y1 
    run =   x2-x1 
    if run == 0:
        if y2 < y1:
            y1, y2 = (y2, y1)
        for y in range(y1,y2+1):
            points.append([x1,y])
    else:
        m = float(rise)/run 
        b = y1 - m * x1 
        if m <= 1 and m >= -1:
            if x2 < x1:
                x1, x2 = (x2, x1 )
            for x in range(x1,x2+1):
                y = int(round(m*x+b))
                points.append([x,y])
        else:
            if y2 < y1:
                y1, y2 = (y2,y1)
            for y in range(y1,y2+1):
                x = int(round((y-b)/m))
                points.append([x,y])
                
                
                
    return points    
def bresenham(x1,y1,x2, y2):  #Line Drawing
    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
    y=y1 
    points = []
    for x in range(x1,x2+1):  
        points.append([x,y])
        slope_error_new+= m_new  
        if (slope_error_new >= 0):  
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)  

            
    return points 