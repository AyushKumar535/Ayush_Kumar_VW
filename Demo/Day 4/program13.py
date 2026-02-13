def moviedecor1(movie):
    def additonalfeatures():
        movie()
        print('''Key Characters
   Coraline Jones: A spunky, curious girl with blue hair.
   The Other Mother (The Beldam): The main antagonist...
   Wybie Lovat: A talkative, eccentric boy...
   The Cat: A sarcastic black cat...

   Themes & Style
   Visual Contrast: muted vs vibrant palette...
   Tone: creepy, unsettling atmosphere...
   Lessons: bravery, appreciating imperfect reality.''')
    return additonalfeatures


def moviedecor2(movie):
    def additonalfeatures():
        movie()
        print('''
   Characters:
   Horton: A dedicated, compassionate elephant.
   The Mayor of Who-ville: Leader of the tiny community.
   Sour Kangaroo: The skeptic.
   Adaptations: 2008 animated film with Jim Carrey & Steve Carell.
        ''')
    return additonalfeatures

def movies():
    movie_name = input('Enter name of the movie: ')
    if movie_name == 'Coraline':
        @moviedecor1
        def coraline():
            print("Coraline (2009) is a dark fantasy stop-motion animated film...")
        coraline()

    elif movie_name == 'Horton Hears a Who!':
        @moviedecor2
        def horton():
            print("Horton Hears a Who! (1954) is a classic Dr. Seuss children’s book...")
        horton()

    else:
        print('Unrecognized movie title')


movies()