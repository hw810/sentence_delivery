__author__ = 'huaidong'

from search_engine import SearchEngine
import urllib
import json


class GuardianAPISearcher(SearchEngine):
    def __init__(self):
        pass

    def search(self, search_string, debug=False):
        query = urllib.urlencode({'q': search_string,
                                  'api-key': '366ckwet6kzd47z57vnzghup'})
        api_url = 'http://content.guardianapis.com/search?{0}'.format(query)

        if __debug__:
            print api_url

        search_results = urllib.urlopen(api_url)
        search_results = search_results.read()
        results = json.loads(search_results)
        response = results['response']
        hits = response['results']
        urls = [h['webUrl'] for h in hits]
        ret = {'urls': urls, 'articles': None}
        return ret
