import wikipediaapi
import webbrowser


class SearchWiki:

    def __init__(self, inputUser):
        self.inputUser = inputUser

    def searchWiki(self):
        wiki = wikipediaapi.Wikipedia('en')

        wikiPage = wiki.page(self.inputUser)
        searchResult = wikiPage.fullurl

        webbrowser.open(searchResult)

        return True
