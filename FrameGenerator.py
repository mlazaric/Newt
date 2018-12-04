from PIL import Image
from Point import Point

class FrameGenerator:
    def __init__(self, root_degree=4, width=720, height=720, x_start=-1, x_end=1, y_start=-1, y_end=1):
        self.root_degree = root_degree

        self.height = height
        self.width = width

        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end

        self.x_increment = (x_end - x_start) / width
        self.y_increment = (y_end - y_start) / height

        self.is_first_iteration = True
        self.points_left = []
        self.last_image = None

    def iterate(self, num_of_iterations=1):
        if self.is_first_iteration:
            img = Image.new('RGB', (self.width, self.height))
            pixels = img.load()

            self.is_first_iteration = False

            for x_offset in range(self.width):
                for y_offset in range(self.height):
                    coord_x = self.x_start + x_offset * self.x_increment
                    coord_y = self.y_start + y_offset * self.y_increment

                    x_n = Point(coord_x + coord_y*1j, self.root_degree)

                    x_n.iterate(num_of_iterations)

                    if not x_n.has_converged:
                        self.points_left.append((x_offset, y_offset, x_n))

                    pixels[x_offset, y_offset] = x_n.get_color()

            self.last_image = img.copy()

            return img
        else:
            img = self.last_image.copy()
            pixels = img.load()

            for (x_offset, y_offset, x_n) in self.points_left:
                x_n.iterate(num_of_iterations)

                pixels[x_offset, y_offset] = x_n.get_color()

            self.points_left = [(x_offset, y_offset, x_n)
                                for (x_offset, y_offset, x_n) in self.points_left
                                if not x_n.has_converged]

            self.last_image = img.copy()

            return img
