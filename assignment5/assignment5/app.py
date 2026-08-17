import datetime
from datetime import timedelta
from typing import List, Optional


import pandas as pd
import altair as alt
import os
import uvicorn
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from strompris import (
    ACTIVITIES,
    LOCATION_CODES,
    fetch_day_prices,
    fetch_prices,
    plot_activity_prices,
    plot_daily_prices,
    plot_prices,
)

#calls FastAPI and set it to app
app = FastAPI()
#definerer directory for bruk med jinja template
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def root1(request: Request) -> dict:
    """ Renders the `strompris.html` template
        with inputs:
        - request
        - location_codes: location code dict
        - today: current date
        Returns:
        - TemplateResponse
    """

    return templates.TemplateResponse(
        "strompris.html",
        {"request": request, "location_codes": LOCATION_CODES, "today": datetime.date.today()},
    )

@app.get('/plot_prices.json')
async def plot(locations: list = Query(default=None), end: datetime.date = datetime.date.today(), days: int = 7) -> alt.Chart:
    """
    Inputs:
    - locations (list from Query)
    - end (date)
    - days (int, default=7)
    all inputs should be optional
    return should be a vega-lite JSON chart (alt.Chart.to_dict())
    produced by `plot_prices`

    """
    #setting default to "all" locations, if Refresh is pushed and no location boxes checked
    if locations == None:
        locations = tuple(LOCATION_CODES.keys())

    #fetching the dataframe
    df1 = fetch_prices(end, days, locations)
    #making the plots
    plot1 = plot_prices(df1)
    plot2 = plot_daily_prices(df1)
    #plot2 = plot_prices

    #concatenating to show both daily prices and average in separate charts
    plot = alt.hconcat(plot1, plot2)

    return plot.to_dict()

# (task 5.6: return chart stacked with plot_daily_prices)
...
# Task 5.6:
@app.get('/activity')
async def root2(request: Request):
    """
    GET /activity` should render the `activity.html` template
    activity.html template must be adapted from `strompris.html`
    with inputs:
    - request
    - location_codes: location code dict
    - activities: activity energy dict
    - today: current date

    """
    return templates.TemplateResponse(
        "activity.html",
        {"request": request, "location_codes": LOCATION_CODES, "activities": ACTIVITIES, "today": datetime.date.today()},
    )

# Task 5.6:

@app.get('/plot_activity.json')
async def plot_activity(location: str = "NO1", activity: str ="shower", minutes: int = 10) -> alt.Chart:
    """
    `GET /plot_activity.json` should return vega-lite chart JSON (alt.Chart.to_dict())
    from `plot_activity_prices`
    with inputs:
    - location (single, default=NO1)
    - activity (str, default=shower)
    - minutes (int, default=10)
    """
    #if location == None:
    #    location = "NO1"
    #fetching the dataframe
    df = fetch_day_prices(datetime.date.today(),location)
    #making the plot
    plot = plot_activity_prices(df,activity,minutes)

    return plot.to_dict()


### documentation Sphinx ###
#defining the path to _build/html - where we want to run the html-files from. It has to end in _build/html
#path to docs/ will depend on the where directory is placed
directory = os.path.abspath('C:/IN4110/IN3110-malina/assignment5/assignment5/docs/_build/html/')
#Makes sure html is run
html = True
#mounting the static files independently to, fastAPI app,
app.mount("/help", StaticFiles(directory=directory, html = html), name='/help')


if __name__ == "__main__":
    # use uvicorn to launch your application on port 5000
    uvicorn.run("app:app", host="127.0.0.1",port=5000,reload=True)
