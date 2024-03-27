import json

movies = []

# read movies file into variable
with open('movies.json', 'r') as openfile:
    # Reading from json file
    movies = json.load(openfile)

while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot filmu")
    print("2. Rādīt visas pievienotas filmas sakartotas pēc reitinga")
    print("3. Rādīt vēl neskatītās filmas")
    print("4. Atzimēt filmu kā skatītu")
    print("5. Dzēst filmu no saraksta")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # https://www.w3schools.com/python/python_dictionaries.asp
        # https://www.w3schools.com/python/python_lists_add.asp
        title = input("Enter movie title: ")
        rating = input("Enter movie rating: ")
        watched = input("Enter True or False if you've watched the film: ")
        x = {
            "title": title,
            "rating": rating,
            "watched": watched,
        }
        movies.append(x)
        pass
    elif choice == "2":
        def sorting(lielakie_rating):
            return int(lielakie_rating["rating"])
        movies.sort(key = sorting, reverse = True)
        print(movies)
        pass
    elif choice == "3":
        def sorting(neskatitas_filmas):
            return int(neskatitas_filmas["watched"])
        movies.sort(key = sorting)
        print(movies)
        pass
    elif choice == "4":
        id = int(input("Enter the index of the movie to mark: "))
        movies[id]["watched"] = True
    elif choice == "5":
        # https://www.w3schools.com/python/python_lists_remove.asp
        id = int(input("Enter the index of the movie to remove: "))
        del movies[id]
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

# writing movies to file
with open("movies.json", "w") as movies_file:
    json.dump(movies, movies_file)
