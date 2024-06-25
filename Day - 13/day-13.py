class Movie:
    def __init__(self, title, available_seats):
        self.title = title
        self.available_seats = available_seats

    def book_seat(self, num_seats):
        if self.available_seats >= num_seats:
            self.available_seats -= num_seats
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title} - Seats Available: {self.available_seats}"

class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        for movie in self.movies:
            print(movie)

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

def main():
    # Menambahkan beberapa film ke dalam daftar
    movie1 = Movie("Inside out 2", 10)
    movie2 = Movie("Interstellar", 5)
    cinema = Cinema()
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)

    while True:
        print("\nDaftar Film:")
        cinema.show_movies()

        movie_title = input("Masukkan judul film yang ingin Anda pesan (atau ketik 'selesai' untuk keluar): ")
        if movie_title.lower() == 'selesai':
            break

        movie = cinema.find_movie(movie_title)
        if movie is None:
            print("Film tidak ditemukan. Silakan coba lagi.")
            continue

        try:
            num_seats = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
        except ValueError:
            print("Jumlah tiket harus berupa angka. Silakan coba lagi.")
            continue

        if movie.book_seat(num_seats):
            print(f"Tiket berhasil dipesan! {num_seats} tiket untuk {movie_title}.")
        else:
            print("Tiket tidak cukup tersedia. Silakan coba lagi.")

    print("\nDaftar Film Terakhir:")
    cinema.show_movies()

if __name__ == "__main__":
    main()
