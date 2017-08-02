import webbrowser


class Movie():
	"""This class stores information about movies."""

	def __init__(self, movie_title, poster_url, trailer_url):
		"""The inputs for this class are
		movie_title, poster_url, and trailer_url"""
		self.title = movie_title
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url

	# play the trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
