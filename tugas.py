class Rectangle:
    def _init_(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        
        self.length = length
        self.width = width

    def calculate_circumference(self):
        return 2 * (self.length + self.width)
    
    def calculate_area(self):
        return self.length * self.width

    def _str_(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"
