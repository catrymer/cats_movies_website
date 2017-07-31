import media
import cats_movies

#instantiate the individual movie objects for the webpage
mrs_henderson_presents = media.Movie("Mrs. Henderson Presents", 
				     "http://www.impawards.com/2005/posters/mrs_henderson_presents_ver2.jpg", 
				     "https://www.youtube.com/watch?v=X858gLx6kuc")

paradise = media.Movie("The Paradise", 
		       "http://cdn-static.sidereel.com/tv_shows/53472/giant_2x/262585-4.jpg", 
		       "https://www.youtube.com/watch?v=M9etSsUgCnw")

delovely = media.Movie("Delovely", 
		       "http://www.impawards.com/2004/posters/de_lovely_ver2.jpg", 
		       "https://www.youtube.com/watch?v=sjqQ1c9EJkY")

moulin_rouge = media.Movie("Moulin Rouge", 
			   "https://cdn.traileraddict.com/content/20th-century-fox/moulin_rouge-6.jpg",
			   "https://www.youtube.com/watch?v=dMSvKpVwavk")

love_actually = media.Movie("Love Actually", 
			    "http://img.moviepostershop.com/love-actually-movie-poster-2003-1010326751.jpg", 
			    "https://www.youtube.com/watch?v=Wj4dHXsza0g")

a_of_gg = media.Movie("Anne of Green Gables", 
		      "https://www.cinematerial.com/media/posters/md/vb/vbd7ddrz.jpg",
		      "https://www.youtube.com/watch?v=czJi_FpLBYY")

much_ado_nothing = media.Movie("Much Ado About Nothing", 
			       "http://img.moviepostershop.com/much-ado-about-nothing-movie-poster-1993-1010243486.jpg", 
			       "https://www.youtube.com/watch?v=__bPqeLkftc")

titanic = media.Movie("Titanic", 
		      "https://images-na.ssl-images-amazon.com/images/I/51n%2BfMMzkqL.jpg",
		      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

thorn_birds = media.Movie("The Thorn Birds", 
			  "https://prodimage.images-bn.com/pimages/0883929206643_p0_v2_s192x300.jpg",
			  "https://www.youtube.com/watch?v=4ZP5D03LlV8")

#add the movies to a list then open the movie page with the list content
movies = [mrs_henderson_presents, paradise, delovely, moulin_rouge, 
	  love_actually, a_of_gg, much_ado_nothing, titanic, thorn_birds]
cats_movies.open_movies_page(movies)
