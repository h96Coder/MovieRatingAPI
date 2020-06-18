from django.db.models import Sum,Count,Avg,F
import smtplib
from email.message import EmailMessage
from MovieApp.models import Movie,Rating
from django.conf import settings




def send_emails():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    sender = settings.SENDER
    senderpass = settings.PASSWORD
    server.login(sender, senderpass)

    moviequeryset=Rating.objects.annotate(avg=Avg('rating'),username=F('movie_name__creator__username'),
                                          email=F('movie_name__creator__email'),movie=F('movie_name__movie_name')).\
                                           values('avg','movie','username','email')
    for movieitem in moviequeryset:
        msg = EmailMessage()
        msg.set_content("Hi "+str(movieitem['username'])+"\n Your Movie: "+str(movieitem['movie'])+
                        " is rated by avg rating : "+str(int(movieitem['avg'])))
        msg['Subject'] = "Movie Rating: "+str(movieitem['movie'])
        msg['From'] = sender
        msg['To'] = movieitem['email']
        server.sendmail(sender, movieitem['email'], msg.as_string())

    server.quit()
