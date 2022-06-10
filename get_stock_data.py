import requests

"""
    Gets some stock data from an api and converts it into a graph.
    <<GOAL>> Send a request with param of <<str: symbol>> (company name_ then returns the relevant data with that 
    company symbol. Gets the latest 5 days close values.
    <<STRETCH GOAL>> Converts company name into <<str: symbol>>.
"""


def get_data_from_api():
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": "MSFT", "outputsize": "compact",
                   "datatype": "json"}
    headers = {
        "X-RapidAPI-Key": "cca6cc9fd3mshe16648624226edcp16fc0bjsnbf9ae908dcb6",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()["Time Series (Daily)"]


raw_data = get_data_from_api()


def get_five_latest_days():
    return_values = [raw_data[x]["4. close"] for x in raw_data]
    return return_values
    # data = raw_data["2022-06-10"]
    # close = data['4. close']



if __name__ == "__main__":
    print(get_five_latest_days())
