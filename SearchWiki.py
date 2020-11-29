import wikipedia
import webbrowser


class SearchWiki:

    def __init__(self, inputUser):
        self.inputUser = inputUser

    def searchWiki(self):

        search = wikipedia.search(self.inputUser)
        searchResult = wikipedia.page(search[0])

        webbrowser.open(searchResult.url)
