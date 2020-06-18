import django
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieRating.settings')
# settings.configure(default_settings=, DEBUG=True)True
django.setup()


from MovieApp.models import Movie,Rating

from django.contrib.auth.models import User

def populatedata():
    u1=User.objects.create_user(username='himanshu',email="hkshraxaxiaai@gmail.com",password='1234')
    u2=User.objects.create_user(username='himan',email="hkshraxzcxiisa@gmail.com",password='1234')
    u3=User.objects.create_user(username='himankumar',email="hkshrasxdsxii@gmaixl.com",password='1234')
    u4=User.objects.create_user(username='himankumar1',email="hkshrxsxsxsaisaxsi@gmail.com",password='1234')
    m1=Movie.objects.create(movie_name='HumTum',creator=u1)
    m2=Movie.objects.create(movie_name='Tum',creator=u2)
    m3=Movie.objects.create(movie_name='Tum2',creator=u3)
    m4=Movie.objects.create(movie_name='Tum3',creator=u4)
    Rating.objects.create(movie_name=m2,rating=4, rater=u1)
    Rating.objects.create(movie_name=m2,rating=3, rater=u3)
    Rating.objects.create(movie_name=m2,rating=4, rater=u4)
    Rating.objects.create(movie_name=m1, rating=5, rater=u2)
    Rating.objects.create(movie_name=m1, rating=3, rater=u3)
    Rating.objects.create(movie_name=m1, rating=2, rater=u4)
    Rating.objects.create(movie_name=m4, rating=3, rater=u2)
    Rating.objects.create(movie_name=m4, rating=3, rater=u1)
    Rating.objects.create(movie_name=m4, rating=2, rater=u3)
    Rating.objects.create(movie_name=m3, rating=2, rater=u1)
    Rating.objects.create(movie_name=m3, rating=1, rater=u2)
    Rating.objects.create(movie_name=m3, rating=2, rater=u4)
if __name__ == '__main__':
    populatedata()
