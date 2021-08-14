import os
import tweepy as tweepy
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site

from .models import DevilName

@receiver(post_save, sender=DevilName)
def tweet_devilname(sender, instance, **kwargs):
    twitter_auth_keys = {
        "consumer_key": os.environ.get('TWITTER_API_KEY', False),
        "consumer_secret": os.environ.get('TWITTER_API_SECRET_KEY', False),
        "access_token": os.environ.get('TWITTER_ACCESS_TOKEN', False),
        "access_token_secret": os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', False),
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )

    api = tweepy.API(auth)

    domain = Site.objects.get_current().domain
    url = DevilName.get_absolute_url(instance)
    full_url= f'https://{domain}{url}'
    char_count = 179
    name = info = (instance.name[:char_count] + '...') if len(instance.name) > char_count else instance.name

    # 21 caracteres
    tweet = f'Novo Nome do Capeta: \'{name}\'.\n\n{full_url}'

    try:
        api.update_status(tweet)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            print('duplicate message')