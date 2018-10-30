from bs4 import BeautifulSoup
import requests


def get_soup(url, hdr='html.parser'):
    r = requests.get(url)
    html = r.text
    return BeautifulSoup(html, hdr)


start_page = 1
end_page = 139

url = 'https://pttweb.tw/board-list?page={}'
all_board = []
for i in range(start_page, end_page):
    print("Processing page {}...".format(i))
    soup = get_soup(url.format(i))
    board_names = soup.findAll("span", {"class": "board-name"})
    for b in board_names:
        all_board.append(b.get_text())

no_set = len(all_board)
all_board = set(all_board)
print(all_board)
print("no_set: ", no_set)
print("with_set", len(all_board))
