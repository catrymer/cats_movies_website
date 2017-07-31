import webbrowser

#define a movie class with the necessary instance variables 
class Movie():
	"""This class stores information about movies."""

	def __init__(self, movie_title, poster_image, youtube_trailer):
		"""The inputs for this class are movie_title, poster_image, and youtube_trailer"""
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

	#play the trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
