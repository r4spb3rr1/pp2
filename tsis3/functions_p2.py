movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_imdb_score_of_one_film_above_5_5(imdb_score):
    if(imdb_score > 5.5):
        return True
    else:
        return False
    
def is_imdb_score_of_films_above_5_5(movies_list):
    imdb_high_score_movies = []
    for i in movies_list:
        if i['imdb'] > 5.5:
            imdb_high_score_movies.append(i)
    return imdb_high_score_movies

def search_for_category(movies_list):
    category = input("Which category do you need? Write here: ")
    for i in movies_list:
        if i['category'] == category:
            print(f"Name of the film: {i['name']}, IMDB Score: {i['imdb']}") 

def average_imdb_score(movies_list):
    s = 0
    ss = 0
    for i in movies_list:
        s += i['imdb']
        ss += 1
    print(f"Average IMDB Score of all movies: {s / ss}") 

def average_imdb_score_by_category(movies_list):
    category = input("Which category do you need? Write here: ")
    s = 0
    ss = 0
    for i in movies_list:
        if i['category'] == category:
            s += i['imdb']
            ss += 1
    print(f"Average IMDB Score of category - {category} is: {s / ss}") 


print(is_imdb_score_of_one_film_above_5_5(movies[0]['imdb']))
print(is_imdb_score_of_films_above_5_5(movies))
search_for_category(movies)
average_imdb_score(movies)
average_imdb_score_by_category(movies)