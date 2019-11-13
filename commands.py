import subprocess
import os
import requests
from bs4 import BeautifulSoup
import random

page = requests.get("https://www.bbc.co.uk/weather/2638678")

soup = BeautifulSoup(page.content, "html.parser")

weather_website = soup.find(class_="wr-day-carousel__scrollable")

weather_data = weather_website.find(class_="wr-value--temperature--c").get_text()

weather_symbol = weather_website.find(class_="wr-weather-type__text").get_text()

def respond(self, response):
    print(response)
    subprocess.call('.\say.exe -m "' + response + "'", shell=True)


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "compliment" in text:
            compliment = ["You're a gift to those around you.", "You're a smart cookie.", "You are awesome!", "You have"
                        " impeccable manners.","You have the best laugh.", "You are the most perfect you there is.",
                        "You're strong.", "Your perspective is refreshing.", "I'm grateful to know y"
                        "ou.", "You light up the room.", "You should be proud of yourself.",
                        "You're more helpful than you realize.","You are really courageous.", "Your kindness is a balm "
                        "to all who encounter it.","You're all that and a super-size bag of chips.","On a scale from 1 "
                        "to 10, you're an 11.","I'm inspired by you.","You're like a ray of sunshine on a really drea"
                        "ry day.","You are making a difference."]
            compliment_no = compliment[random.randint(0, 19)]
            subprocess.call('.\say.exe -m "' + compliment_no)

        if "what" in text and "name" in text:
            if "my" in text:
                subprocess.call('.\say.exe -m "' + "You haven't told me your name yet. Please tell me it.")
            else:
                subprocess.call('.\say.exe -m "' + "My name is D.P.A (Dhhyey's Personal Assist). How are you?")
        if "what" in text and "weather" in text:
            if "weather" in text:
                subprocess.call('.\say.exe -m "' + "The weather today will be " + weather_symbol + ". And it will be" + weather_data)
            else:
                subprocess.call('.\say.exe -m "' + "Sorry I didn't catch that")


