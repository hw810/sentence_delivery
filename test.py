__author__ = 'hd'


from search_engine.guardian_api_search import GuardianAPISearcher

mysearcher = GuardianAPISearcher()
ret = mysearcher.search(search_string="world", debug=True)

