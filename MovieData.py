from imdb import IMDb
im = IMDb()
print()
m = im.get_movie('0371746')
print(m.data.keys())
print()
print("Movie Data using IMDb id")
print("imdbID : ",m.data['imdbID'])
print("Title : ",m.data['title'])
print("Year : ",m.data['year'])
print("Genre : ",m.data['genres'])
print("Director : ",m.data['director'])
print("Cast : ",m.data['cast'])
print("Plot Outline : ",m.data['plot outline'])
print("Rating : ",m.data['rating'])
print("Box Office : ",m.data['box office'])
print("Plot : ",m.data['plot'])
print("Synopsis : ",m.data['synopsis'])

def moviedata():
    print()
    print("Search for Movie Details")
    name=input("Enter Movie Name : ")
    val = im.search_movie(name)
    if (val == []):
        print("No Results Found")
    else:
        print(val)

moviedata()
