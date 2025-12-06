import sqlite3
import matplotlib.pyplot as plt
from config import OPENCAGE_API_KEY #0c4b6acdae42492cb5176f4adae721db
import requests

def get_coordinates(location):
    url = 'https://api.opencagedata.com/geocode/vq/json'
    params = 