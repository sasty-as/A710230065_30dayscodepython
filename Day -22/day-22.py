# Implementasi private variabel dan getter and setter

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    # Getter methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter methods
    def set_make(self, make):
        if isinstance(make, str) and make:
            self.__make = make
        else:
            raise ValueError("Make must be a non-empty string.")

    def set_model(self, model):
        if isinstance(model, str) and model:
            self.__model = model
        else:
            raise ValueError("Model must be a non-empty string.")

    def set_year(self, year):
        if isinstance(year, int) and year > 1885:  # First car was invented around 1885
            self.__year = year
        else:
            raise ValueError("Year must be an integer greater than 1885.")

    # Method to return a string representation of the Car object
    def __str__(self):
        return f"{self.__year} {self.__make} {self.__model}"

# Membuat objek Car
car = Car("Honda", "Civic", 2022)

# Mengakses variabel privat melalui metode getter
print(car.get_make())  # Output: Honda
print(car.get_model()) # Output: Civic
print(car.get_year())  # Output: 2022

# Mengubah nilai variabel privat melalui metode setter
car.set_make("Toyota")
car.set_model("Corolla")
car.set_year(2023)

# Mengakses variabel privat yang telah diubah
print(car.get_make())  # Output: Toyota
print(car.get_model()) # Output: Corolla
print(car.get_year())  # Output: 2023

# Menggunakan metode __str__
print(car)  # Output: 2023 Toyota Corolla

