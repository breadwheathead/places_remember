import requests
from collections import OrderedDict
from urllib.parse import urlencode, urlunparse

from django.conf import settings


def save_avatar(backend, user, response, *args, **kwargs):
    """ Save avatar in media/avatar folder """
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields='photo_400_orig',
                                                access_token=response['access_token'],
                                                v='5.131')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['photo_400_orig']:
        user.avatar = get_avatar(data['photo_400_orig'], user.username)

    user.save()


def get_avatar(path, username):
    """ Get avatar by API vk and return path to file """
    response = requests.get(path)
    avatar_name = f'{username}.jpg'
    with open(f'{settings.MEDIA_ROOT}/images/avatars/{avatar_name}', 'wb') as file:
        file.write(response.content)
    return f'/images/avatars/{avatar_name}'
