import requests
from decouple import config
from typing import List

"""
    Gets some stock data from an api and converts it into a graph.
    <<GOAL>> Send a request with param of <<str: symbol>> (company name_ then returns the relevant data with that 
    company symbol. Gets the latest 5 days close values.
    <<STRETCH GOAL>> Converts company name into <<str: symbol>>.
"""


def get_ticker_symbol(company: str) -> List[dict]:
    """
    Gets a list of suggestions for ticker symbols based on user input.
    """
    # send a GET request with the company name as keyword in the url
    res = requests.get(f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}'
                       f'&apikey={config("SECRET_API_KEY")}')
    ticker_symbol = res.json()["bestMatches"]
    return [{
        'symbol': current_selected_data['1. symbol'],
        'name': current_selected_data['2. name']
    } for current_selected_data in ticker_symbol[:5]]


def get_data_from_api(ticker_symbol: int) -> dict:
    """
    Gets the stock data from the rapidapi link.
    """
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": f"{ticker_symbol}", "outputsize": "compact",
                   "datatype": "json"}
    headers = {
        "X-RapidAPI-Key": f"{config('SECRET_API_KEY')}",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['Time Series (Daily)']


def get_most_recent_days(raw_data: dict, day_range: int) -> List[dict]:
    """
    Returns relevant stock data for the date range provided.
    """
    return_values = [{
        'date': current_selected_data,
        'open': raw_data[current_selected_data]['1. open'],
        'high': raw_data[current_selected_data]['2. high'],
        'low': raw_data[current_selected_data]['3. low'],
        'close': raw_data[current_selected_data]['4. close']
    } for current_selected_data in raw_data]
    return return_values[:int(day_range)]


if __name__ == "__main__":
    company = input("Please enter company: ")
    day_range = int(input("Please enter a day range: "))
    print(get_most_recent_days(get_data_from_api(get_ticker_symbol(company)[0]['symbol']), day_range))
