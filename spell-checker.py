import enchant
import sys

#accept the movie name from command line arguments
input_movie_name = sys.argv[1]

#load the personal word list dictionary
movies_dict = enchant.PyPWL("movies.txt")

#check if the word exists in the dictionary
word_exists = movies_dict.check(input_movie_name)
print("word exists: ", word_exists)

if not word_exists:
	#get suggestions for the input word if the word doesn't exist in the dictionary
	suggestions = movies_dict.suggest(input_movie_name)

	print ("input:", input_movie_name)
	print("suggestions:", suggestions)
