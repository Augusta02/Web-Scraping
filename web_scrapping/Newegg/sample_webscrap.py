import bs4
import requests


url = 'https://archive.ics.uci.edu/ml/datasets.php'

lesponse = requests.get(url)