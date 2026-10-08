class Rectangle:
    def _init_(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        
        self.length = length
        self.width = width