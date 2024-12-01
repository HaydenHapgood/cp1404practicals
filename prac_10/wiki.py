import wikipedia

while True:
    wiki_search = input("Enter page title: ")
    if wiki_search == '':
        print("Thank you.")
        break
    try:
        summary = wikipedia.summary(wiki_search)
        page_title = wikipedia.search(wiki_search)[0]
        page_url = wikipedia.page(page_title).url
        print(f"\n{page_title}\n{summary}\n{page_url}\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"\nWe need a more specific title. Try one of the following, or a new search:\n{e.options}\n")
    except wikipedia.exceptions.PageError:
        print("\nPage id does not match any pages. Try another id!\n")
