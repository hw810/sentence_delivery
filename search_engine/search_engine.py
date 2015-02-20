

class SearchEngine:
    """
    This is an abstract class of a search engine for sentences searching

    """
    
    def search(self, search_string):
        raise NotImplementedError("Subclass must implement abstract method")
