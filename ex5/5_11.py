def is_inside(point, rect):
    # x1,y1 = point
    #x2,y2,width,height = rect
    x1 = point[0]
    y1 = point[1]
    x2 = rect[0]
    y2 = rect[1]
    width = rect[2]
    height = rect[3]
    if x2 <= x1 <= x2 + width and y2 <= y1 <= y2 + height:
        return True
    return False
print(is_inside([100,120],[140,60,100,200]))
print(is_inside([200,120],[140,60,100,200]))