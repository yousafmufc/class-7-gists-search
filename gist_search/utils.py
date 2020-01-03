import requests

BASE_URL = 'https://api.github.com/users/{username}/gists'


def get_gists(username):
    url = BASE_URL.format(username=username)
    resp = requests.get(url, params={'per_page': 100})
    if not resp.ok:
        return None
    return resp.json()
  
if __name__ == '__main__': # this will cause below code to run only when we are explicitly focused on this current module utils.py
  
  gists = get_gists('gvanrossum')

  first_three_gists = gists[:3]

  for gist in first_three_gists:

    print('{} - {}'.format(gist['id'], gist["description"]))
    
  
  
  