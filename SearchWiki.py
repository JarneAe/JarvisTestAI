import wikipediaapi
import webbrowser


class SearchWiki:

    # Initialize the inputUser variable
    def __init__(self, inputUser):
        self.inputUser = inputUser

    # Search a certain wikipedia page and open it
    def searchWiki(self):
        wiki = wikipediaapi.Wikipedia('en')

        if wiki.page(self.inputUser).exists():
            wikiPage = wiki.page(self.inputUser)
            searchResult = wikiPage.fullurl
            webbrowser.open(searchResult)
        else:
            print("Can't find wikipedia page.")

        return True
