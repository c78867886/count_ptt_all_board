from bs4 import BeautifulSoup
from collections import OrderedDict
import requests


def get_soup(url, hdr='html.parser'):
    r = requests.get(url)
    html = r.text
    return BeautifulSoup(html, hdr)


def remove_duplicate_order_preserved(original_list):
    seen = set()
    seen_add = seen.add
    return [x for x in original_list if not (x in seen or seen_add(x))]


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

all_board = remove_duplicate_order_preserved(all_board)

with open("all_board.txt", 'w', encoding="utf-8") as f:
    f.write('\n'.join(all_board))

print("The number of all boards: {}".format(len(all_board)))
