import re
from typing import Tuple
from requesting_urls import *

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

...


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029

    year = r"(?P<year>\b[1-2][0-9]{3}\b)"

    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>\b[1-9]\b|\b[0][1-9]\b|\b[1][0-9]\b|\b[2][0-9]\b|\b[3][0-1]\b)"

    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]ay\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]ug(?:ust)?\b"
    sep = r"\b[sS]ep(?:tember)?\b"
    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"


    month_numbers = r"\b[1-9]\b|\b[1][0-2]\b|\b[0][1-9]\b"
    month = rf"(?P<month>{month_numbers}|{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct}|{nov}|{dec})"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    months = {"jan": '01', "feb": '02', "mar": '03', "apr": '04', "may": '05', "jun": '06', "jul": '07', "aug": '08', "sep": '09', "oct": '10', "nov": '11', "dec": '12',
    "January": '01', "February": '02', "March": '03', "April": '04', "May": '05', "June": '06', "July": '07', "August": '08', "September": '09', "October": '10', "November": '11', "December": '12'}

    # If already digit do nothing
    if s.isdigit():
        ...

    # Convert to number as string

    else:
        for i in months:
            if s == i:
                s = months[i]
    return s

def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """

    days = {"1": '01', "2": '02', "3": '03', "4": '04', "5": '05', "6": '06', "7": '07', "8": '08', "9": '09'}

    for i in days:
        if n == i:
            n = days[i]
    return n

def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    year, month, day = get_date_patterns() #det er en tuple som returneres


    # Date on format YYYY-MM-DD
    ISO = rf"{year}-{month}-{day}" #r"\b(?:0\d|1[0-2])\b"

    # Date on format DD/MM/YYYY
    DMY = rf"{day}\s{month}\s{year}" #("%s %s %s" %(day,month,year))

    # Date on format MM/DD/YYYY
    MDY = rf"{month}\s{day},\s{year}" #("%s %s %s" %(month,day,year))

    # Date on format YYYY/MM/DD
    YMD = rf"{year}\s{month}\s{day}" #("%s %s %s" %(year,month,day))

    DATE = rf"{year}/{month}/{day}"
    # list with all supported formats
    formats = [ISO,DMY,MDY,YMD]
    dates = []

    ISO_date, DMY_date, MDY_date, YMD_date = [], [], [], []

    # find all dates in any format in text
    #Year/Month/Day
    # separates the lists to make it easier to work with
    for format in formats:
        if format == ISO:
            ISO_date.append(re.findall(format,text))
        if format == DMY:
            DMY_date.append(re.findall(format,text))
        if format == MDY:
            MDY_date.append(re.findall(format,text))
        if format == YMD:
            YMD_date.append(re.findall(format,text))

    # FLATTEN ALL THE 4 LISTS AND MAKE SURE THEY GET THE RIGHT FORMAT
    # put them all into dates, after running them through zero_pad and convert_month
    flat1 = []
    for sublist in ISO_date:
        for item in sublist:
            flat1.append(item)
    for i in range(len(flat1)):
        digit = convert_month(flat1[i][1])
        zero_padded = zero_pad(flat1[i][2])
        dates.append(flat1[i][0] + "/" + digit + "/" + zero_padded)

    flat2 = []
    for sublist in DMY_date:
        for item in sublist:
            flat2.append(item)
    for i in range(len(flat2)):
        digit = convert_month(flat2[i][1])
        zero_padded = zero_pad(flat2[i][0])
        dates.append(flat2[i][2] + "/" + digit + "/" + zero_padded)

    flat3 = []
    for sublist in MDY_date:
        for item in sublist:
            flat3.append(item)
    for i in range(len(flat3)):
        digit = convert_month(flat3[i][0])
        zero_padded = zero_pad(flat3[i][1])
        dates.append(flat3[i][2] + "/" + digit + "/" + zero_padded)
    print(flat3)
    flat4 = []
    for sublist in YMD_date:
        for item in sublist:
            flat4.append(item)
    for i in range(len(flat4)):
        digit = convert_month(flat4[i][1])
        zero_padded = zero_pad(flat4[i][2])
        dates.append(flat4[i][0] + "/" + digit + "/" + zero_padded)

    # Write to[0] file if wanted
    if output:
        print(f"Writing to: {output}")

        file = open(f'{output}','w', encoding = "utf-8")
        file.write("%s" %(dates))
        file.close()

    return dates
