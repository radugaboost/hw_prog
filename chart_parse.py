from requests import get
from pprint import pprint
from bs4 import BeautifulSoup
from config import (
    YANDEX_URL, HEADERS, CHART_LINE, AUTHOR, TRACK, HTTP_OK
)

if __name__ == "__main__":
    response = get(YANDEX_URL, headers=HEADERS)

    if response.status_code == HTTP_OK:
        chart = dict()
        soup = BeautifulSoup(response.text, "lxml")
        lines = soup.find_all("div", class_=CHART_LINE)
        for line in enumerate(lines):
            author = line[1].find("a", class_=AUTHOR).text
            track = line[1].find("a", class_=TRACK).text
            chart[line[0] + 1] = {
                author: " ".join(track.strip().split())
            }

    pprint(chart)
