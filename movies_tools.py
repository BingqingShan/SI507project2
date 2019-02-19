import csv
import random

with open("movies_clean.csv", "r") as f:
	reader = csv.reader(f)
	header = next(reader)
	total = []
	for i in reader:
		total.append(i) #create a list of movies

total_number=len(total) # this is the total number of movies




class Movie:
	def __init__(self):
		random_movie=random.choice(total)
		self.title= random_movie[0] #title: single movie title
		self.rating= random_movie[14] #rating: single movie rating
	def __str__(self):
		return '{} | {}'.format(self.title, self.rating)


# if __name__ == "__main__":
	# print(Movie())
	# print(total_number)
