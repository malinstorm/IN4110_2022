#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

"""

import datetime
from datetime import timedelta
import altair as alt
import pandas as pd
import requests
import requests_cache
from pandas.io.json import json_normalize
from vega_datasets import data
# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()


# task 5.1:


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    Arguments:
    date (datetime.date) --> the date picked to fetch data from
    location (str) --> location(s) (codes) we want to gather data from

    Returns Pandas DataFrame
    """
    if date is None:
        #setting the date to today, if no date is provided as an argument
        date = datetime.date.today()

    # asserting date doesn't go longer back than 2022-10-02 (but including day == 1, for months preceding october)
    assert date.year >= 2022 and date.month >= 10 and date.day >= 2 or date.year >= 2022 and date.month >= 11 and date.day >= 1

    #if/else to assure zero padded day/month
    if date.day < 10:
        day = "0" + str(date.day)
    else: day = str(date.day)
    if date.month < 10:
        month = "0" + str(date.month)
    else: month = str(date.month)
    # defining the right url-format to reach the website https://hvakosterstrommen
    url = "https://hvakosterstrommen.no/api/v1/prices/" + str(date.year) + "/" + month + "-" + str(day) + "_" + location + ".json"
    #get the html
    r = requests.get(url)

    # convert html to pandas dataframe
    df = pd.read_json(r.text)
    #columns wanted from dataframe
    df['location'] = location
    wanted = ['NOK_per_kWh','time_start','location']
    #picking out the wanted columns of df
    df = df[wanted]
    #setting column time_start to datetime-type, utc = True
    df['time_start'] = pd.to_datetime(df['time_start'],utc = True).dt.tz_convert("Europe/Oslo")

    #returning a df with wanted, hourly based data
    return df

# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen"
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys())
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Arguments:
    end_date (datetime.date) --> the last date picked to fetch data from
    days (int) default = 7 --> the number of days we want to gather data from
    locations (tuple) --> location(s) (codes) we want to gather data from

    Returns Pandas DataFrame

    """
    if end_date is None:
        #setting the date to today, if no end_date is provided as an argument
        end_date = datetime.date.today()

    # need a starting point for fetching data. To also get the end_date counted DAYS + 1
    start_date = end_date - timedelta(days=days-1)

    # make an empty DataFrame for concat
    df = pd.DataFrame()

    #make call for fetch_day_prices() number of calls = days
    for day in range(days):
        for key in locations:
            df_temp = fetch_day_prices(datetime.date(start_date.year,start_date.month,start_date.day), key)
            loc = LOCATION_CODES[key]
            #adding additional columns for location code and location name
            df_temp['location'] = loc
            df_temp['location_code'] = key
            df = pd.concat([df,df_temp]) #concatinating accumulated data in final df
        #incrementing the variable start_date to fetch data from
        start_date += timedelta(days=1)
    #returning df with all the wanted data
    return df
# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    Plotting to x-axis (time_start) and y-axis (NOK_per_kWh)  respectively
    Data will be shown as lines
    The graph will show daily prices for location(s)

    Arguments: Pandas Dataframe
    - time_start (datetime.date)
    - NOK_per_kWh (float)
    - color --> each location gets its own line and color
    - tooltip --> tooltip shows columns of differences in the dataset (price: last hour, yesterday, last week)

    Return value is an altair chart based on columns picked from df

    """

    #add columns to compare prices for last_hour, yesterday and last week - same hour
    df['last_hour'] = df['NOK_per_kWh'].diff()
    df['yesterday'] = df['NOK_per_kWh'].diff(periods=24)
    df['last_week'] = df['NOK_per_kWh'].diff(periods=24*7)

    # make chart
    chart = alt.Chart(df).mark_line().encode(
        x= 'time_start',
        y= 'NOK_per_kWh',
        color = 'location',
        tooltip=['location', 'time_start', 'NOK_per_kWh', 'last_hour', 'yesterday', 'last_week']
        )

    return chart
# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    Data will be shown as lines
    The graph will show average daily prices for location(s), daily/hourly based

    Arguments: Pandas dataframe
    - yearmonthdate(hours)(time_start) = date, to make sure that average is calculated for each day in dataset
    - mean(NOK_per_kWh) to calculate the mean
    - M for calculated mean - 1-day range of data in dataset

    Return value is an altair chart based on columns picked from df
    """

    df2 = df #making a new dataframe-var
    # checking if dayrange == 1 by feching the dates
    df2['day'] = pd.DatetimeIndex(df2['time_start']).day
    arr = df2['day'].to_numpy() #converting to np.arr

    #if all the days in dataframe are the same, then day == 1
    if (arr[0] == arr).all():
        df_group = df2.groupby("location") #finds the number of locations the search is for
        df_columns = df_group[["NOK_per_kWh"]] ## groups by kWh related to each locations
        Mean = df_columns.mean() #taking the mean

        df3 = [] #list to store the average values 24 times each, for plotting
        for row in range(len(Mean)):
            for col in range(24):
                df3.append(Mean['NOK_per_kWh'][row])
        #adding the list as a new column to df2
        df2['M'] = df3

        #making a 1-day based chart for avrages in the picked location(s)
        chart = alt.Chart(df2).mark_line().encode(
                x = 'yearmonthdatehours(time_start)',
                y = 'M',
                color = 'location'
                )
    #plotting for days > 1 in the picked location(s)
    else:
        chart = alt.Chart(df).mark_line().encode(
            x = 'yearmonthdate(time_start)',
            y = 'mean(NOK_per_kWh)',
            color = 'location'
            )

    return chart
# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    "shower": 30,
    "baking": 2.5,
    "heat": 1
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10.0
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Inputs:
    - pandas Dataframe
    - activity: (str) default = "shower"
    - minutes: (float) default = 10.0

    Return value is an altair chart based on columns picked from df
    """
    price = 30 #default for shower

    #Calculating price for activity - df unit = kWh, ACTIVITY unit = kW
    for key in ACTIVITIES:
        if key == activity:
            price = ACTIVITIES[key]

    price = float(price*minutes/60) #converting to kW

    assert minutes <= 60 #asserting that minutes cannot override

    # adding rows to dataframe
    df['Price'] = df['NOK_per_kWh']*price
    df['Activity'] = activity

    # getting name of town to display next to graph, adding location to dataframe
    for key in LOCATION_CODES:
        if key == df['location'].values[1]:
            df['location'] = LOCATION_CODES[key]

    chart = alt.Chart(df).mark_line().encode(
        x= 'time_start',
        y= 'Price',
        color = 'location'
        )

    return chart


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
