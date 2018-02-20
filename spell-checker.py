import enchant
import sys

#accept the movie name from command line arguments
input_movie_name = sys.argv[1]

#load the personal word list dictionary
my_dict = enchant.PyPWL("movies.txt")

#get suggestions for the input word
suggestions = my_dict.suggest(input_movie_name)

print ("input:", input_movie_name)
print("suggestions:", suggestions)
