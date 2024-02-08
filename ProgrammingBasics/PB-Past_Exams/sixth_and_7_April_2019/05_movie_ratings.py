from sys import maxsize

number_of_films = int(input())

max_rating = -maxsize
max_film = ""
min_rating = maxsize
min_film = ""
sum_rating = 0

for _ in range(number_of_films):
    film_name = input()
    film_rating = float(input())

    sum_rating += film_rating

    if film_rating > max_rating:
        max_rating = film_rating
        max_film = film_name

    if film_rating < min_rating:
        min_rating = film_rating
        min_film = film_name

average_rating = sum_rating / number_of_films

print(f"{max_film} is with highest rating: {max_rating:.1f}")
print(f"{min_film} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
