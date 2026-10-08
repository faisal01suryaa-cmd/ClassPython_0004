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

    def __str__(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"

if __name__ == "__main__":
    try:
        rect = Rectangle(3, 2)
        print(rect)
        circumference = rect.calculate_circumference()
        print(f"Keliling: {circumference} cm")
        area = rect.calculate_area()
        print(f"Luas: {area} cm²")
    except ValueError as e:
        print(f"Error: {e}")