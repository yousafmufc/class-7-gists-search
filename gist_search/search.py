from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
      
    
    results = []
    
    gists = get_gists(username)
    
    if gists is None:
      print("User {} has no gists to share".format(username))
      
      return  # By default this will return None
    
    for gist in gists:
      
      if description and description.lower() not in gist['description'].lower():
        continue
        
      
      if file_name:
        matched = False #Defining this just so we don't have to append gist inside the for loop and we can use break/continue.
        for fname, fbody in gist['files'].items():
          if file_name in fname:
            matches = True
            break
          if not matched:
            continue
      results.append(gist)
            
    
    
    return results
