import requests
from bs4 import BeautifulSoup

def get_horoscope_by_day(zodiac_sign: int, day: str):
    """Get a horoscope for the day"""
    if not "-" in day:
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
            )
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    
    return data.p.text

def get_horoscope_by_week(zodiac_sign: int):
    """Get a horoscope for the week"""
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    
    return data.p.text


def get_horoscope_by_month(zodiac_sign: int):
    """Get a horoscope for the month"""
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    
    return data.p.text



