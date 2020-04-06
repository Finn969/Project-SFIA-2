#! usr/bin/python

def starsign(d):
    ymdlist= d.split("-")
    month = int(ymdlist[1])
    day = int(ymdlist[2])

    zodiac = ''

    if month == 3 and day > 20 or month == 4 and day <= 19:
        zodiac = "Aries"
    elif month == 4 and day > 19 or month == 5 and day <= 20:
        zodiac = "Taurus"
    elif month == 5 and day > 20 or month == 6 and day <= 20:
        zodiac = "Gemini"
    elif month == 6 and day > 20 or month == 7 and day <= 22:
        zodiac = "Cancer"
    elif month == 7 and day > 22 or month == 8 and day <= 22:
        zodiac = "Leo"
    elif month == 8 and day > 22 or month == 9 and day <= 22:
        zodiac = "Virgo"
    elif month == 9 and day > 22 or month == 10 and day <= 22:
        zodiac = "Libra"
    elif month == 10 and day > 22 or month == 11 and day <= 21:
        zodiac = "Scorpio"
    elif month == 11 and day > 21 or month == 12 and day <= 21:
        zodiac = "Sagittarius"
    elif month == 12 and day > 21 or month == 1 and day <= 19:
        zodiac = "Capricorn"
    elif month == 1 and day > 19 or month == 2 and day <= 18:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"
    
    return zodiac