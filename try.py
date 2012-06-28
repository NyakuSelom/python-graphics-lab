from graphics import *
class Wheel:
    def __init__(self,centre, tire_radius,wheel_radius):
        self.tire_circle = Circle(centre,tire_radius)
        self.wheel_circle = Circle(centre,wheel_radius)

    def draw(self):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move(self,dx,dy):
        self.tire_circle.move(dx,dy)
        self.wheel_circle.move(dx,dy)

    def set_colour(self,tire_colour,wheel_colour):
        self.tire_circle.setFill(tire_colour)
        self.wheel_circle.setFill(wheel_colour)

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_centre(self):
        return self.tire_circle.getCenter()

    

win = GraphWin('Selom Wheel',320,240)

speed = Wheel(Point(160,120),70,50)
