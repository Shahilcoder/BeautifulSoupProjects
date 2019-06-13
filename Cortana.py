import requests
import bs4

#-----------------------------------------------------------------------------------------
def intro(soup):

    try:
        title = soup.find('h1', id="firstHeading").text
        full_data = soup.find('div', class_="mw-parser-output").contents

        return title, full_data

    except Exception as e:
        print(e.__class__, e, sep="\n")

#--------------------------------------------------------------------------------------------
def get_data(tosearch="Goku"):

    try:
        print('wait a second...\n')
        result = requests.get("https://en.wikipedia.org/wiki/{}".format(tosearch))
        soup = bs4.BeautifulSoup(result.text, 'html.parser')
        title, data = intro(soup)

        return title, data
    
    except requests.exceptions.ConnectionError:
        print("Sorry master, But it seems like my internet access is disabled")

    except Exception as e:
        print(e, e.__class__, sep="\n")

#---------------------------------------------------------------------------------------
def print_data(title, full_data):
    print("\t\t\t{}".format(title.upper()))
    for data in full_data:
        if data is not None:
            if data.name == 'h2':
                print("\t\t\t{}".format(data.text.upper()), end="\n\n")
            elif data.name == 'p':
                print(data.text)
            else:
                continue

#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    title, data = get_data()
    print_data(title, data)
    x = input()
    exit()
