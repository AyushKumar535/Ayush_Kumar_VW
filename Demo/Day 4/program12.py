def moviedecor1(movie):
   def additonalfeatures():
      movie()
      print('''Key Characters
   Coraline Jones: A spunky, curious girl with blue hair.
   The Other Mother (The Beldam): The main antagonist who transforms from a sweet maternal figure into a terrifying spider-like witch.
   Wybie Lovat: A talkative, eccentric boy created specifically for the film to act as Coraline's friend (he is not in the original book).
   The Cat: A sarcastic black cat that can travel between worlds and speak in the Other World.

   Themes & Style
   Visual Contrast: The film uses a muted, grey palette for the real world and vibrant, hyper-saturated colours for the Other World to emphasise its deceptive allure.
   Tone: It is widely noted for its "creepy" and unsettling atmosphere, often categorized as horror for children.
   Lessons: Major themes include the dangers of "the grass is always greener" mentality, the importance of bravery, and appreciating imperfect reality. ''')
   return additonalfeatures

def demodecor(movie):
  def inner():
    movie()
    print("Blah blah blah blah")
  return inner

@demodecor
@moviedecor1
def movies():
   movie_name = input('Enter name of the movie: ')
   if movie_name == 'Coraline':
      print("Coraline (2009) is a dark fantasy stop-motion animated film directed by Henry Selick and based on Neil Gaiman’s 2002 novella.")
   else:
      print('unrecognized movie title')
      
movies()