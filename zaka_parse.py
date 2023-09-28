from requests import get
from json import dump
from bs4 import BeautifulSoup
from config import (
    ZAKA_URL, HEADERS, HTTP_OK, GAMES_CONTAINER,
    GAMES_BLOCK, GAME_NAME, GAME_PRICE, ZAKA_JSON_NAME,
    ZAKA_PAGES, JSON_INDENT
)

if __name__ == "__main__":
    all_games = dict()
    for page in range(*ZAKA_PAGES):
        url = ZAKA_URL.format(page)
        response = get(url, headers=HEADERS)
        if response.status_code == HTTP_OK:
            soup = BeautifulSoup(response.text, "lxml")
            container = soup.find("div", class_=GAMES_CONTAINER)
            games = container.find_all("a", class_=GAMES_BLOCK)
            for game in games:
                try:
                    name = game.find("div", class_=GAME_NAME).text
                    price = game.find("div", class_=GAME_PRICE).text
                    all_games[name] = " ".join(price.replace("c", "₽").strip().split())
                except Exception:
                    continue

    with open(ZAKA_JSON_NAME, 'w') as json_file:
        dump(all_games, json_file, ensure_ascii=False, indent=JSON_INDENT)
