import math
class GradientDescent :
    def __init__(self, f, initial_point) :
        self.point = initial_point
        self.function = f

    def compute_gradient(self, delta) :
        gradient = []
        for index in range(len(self.point)) :
            new_points = []
            new_points_2 = []
            for point_index in range(len(self.point)) :
                if point_index == index :
                    new_points.append(self.point[index] + 0.5 * delta)
                    new_points_2.append(self.point[index] - 0.5 * delta)
                else :
                    new_points.append(self.point[index])
                    new_points_2.append(self.point[index])
            gradient_part = (self.function(*new_points) - self.function(*new_points_2))/ delta
            gradient.append(gradient_part)
        return gradient
    
    def descend(self, alpha, delta, num_steps) :
        for _ in range(num_steps) :
            gradient = self.compute_gradient(delta)
            for index in range(len(self.point)) :
                self.point[index] = self.point[index] - alpha * gradient[index]