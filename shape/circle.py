class Circle:

    def __init__(self, a, radius):
        self.radius = radius
        self.centre = a
    
    def __contains__(self, b):
        self.zhupoint = b
        d = (self.zhupoint[0] - self.centre[0])**2 + (self.zhupoint[1]
                                                      - self.centre[1])**2
        if d <= self.radius**2:
            return True
        else:
            return False