import HTMLParser
import csv

class LotoHTMLParser(HTMLParser.HTMLParser):

    def __init__(self, csv_path):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False
        self.counter = 0
        self.csv_path = csv_path
        self.data = []
        self.temp_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True
            self.counter += 1

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_td = False

    def handle_data(self, data):
        if self.in_td is True:
            self.temp_data.append(data)
        if self.counter == 7:
            self.data.append(self.temp_data)
            self.temp_data = []
            self.counter = 0

    def get_data(self):
        return self.data

csv_path = 'data/archive.csv'
parser = LotoHTMLParser(csv_path)

with open('data/table.txt', 'r') as file:
    table = file.read()
parser.feed(table)

with open(csv_path, "wb") as f:
    writer = csv.writer(f)
    writer.writerows(parser.get_data())
