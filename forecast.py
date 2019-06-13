import requests
from bs4 import BeautifulSoup as Bsoup

def get_data(result):
    soup = Bsoup(result.text, 'html.parser')

    Day = soup.find("div", class_="today_nowcard-main component panel today-card-other-fog")

    Place = Day.header.h1.contents[0]

    Last_Update = Day.find("p", class_="today_nowcard-timestamp").span.text + Day.find("p", class_="today_nowcard-timestamp").span.next_sibling.text

    temp = Day.find("div", class_="today_nowcard-temp")

    weather_type = Day.find("div", class_="today_nowcard-phrase")

    feels_like = Day.find("div", class_="today_nowcard-feels")    

    UV_index = list(Day.find("div", class_="today_nowcard-hilo").stripped_strings)
    UVstring = "".join(UV_index)
    UV_index_text = UVstring[0:4] + " " + UVstring[4:7] + "\n" + UVstring[7:15] + " " + UVstring[15:]

    return [Place, Last_Update, temp, weather_type, feels_like, UV_index_text]

def forecast(Data):
    print("\t\t", Data[0])
    print(Data[1])
    print(Data[2].text)
    print(Data[3].string)
    print(Data[4].text)
    print(Data[5])

def main():
    result = requests.get('https://weather.com/en-IN/weather/today/l/22.57,88.42?par=google')
    Data = get_data(result)
    forecast(Data)
    x = input()

if __name__ == '__main__':
    main()
