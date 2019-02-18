import csv
import random

with open("movies_clean.csv", "r") as f:
	reader = csv.reader(f)
	header = next(reader)
	total = []
	for i in reader:
		total.append(i)
	list = []
	for i in range(len(total)):
		title = total[i][0]
		rating = total[i][14]
	# print(list)
total_number=len(total)
# total_number = len(total) # the total number of movies
# print(total_number)
# print(list[0])
# list : the total of movie+rating as a list in a big list
#title: single movie title
#rating: single movie rating


class Movie:
	def __init__(self):
		random_movie=random.choice(total)
		self.title= random_movie[0]
		self.rating= random_movie[14]
	def __str__(self):
		return '{} | {}'.format(self.title, self.rating)


# if __name__ == "__main__":
	# print(Movie())
	# print(total_number)
