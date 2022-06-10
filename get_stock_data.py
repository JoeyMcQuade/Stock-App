import requests

"""
    Gets some stock data from an api and converts it into a graph.
    <<GOAL>> Send a request with param of <<str: symbol>> (company name_ then returns the relevant data with that 
    company symbol. Gets the latest 5 days close values.
    <<STRETCH GOAL>> Converts company name into <<str: symbol>>.
"""


class StockData:

    def __init__(self):
        self.raw_data = {}

    def get_data_from_api(self) -> any:
        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": "KLJAD", "outputsize": "compact",
                       "datatype": "json"}
        headers = {
            "X-RapidAPI-Key": "cca6cc9fd3mshe16648624226edcp16fc0bjsnbf9ae908dcb6",
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        try:
            if self.check_there_is_valid_data(response):
                self.raw_data = response.json()["Time Series (Daily)"]
        except:
            print("Could not collect data.")

    def check_there_is_valid_data(self, response):
        if not response.content or response.status_code == 404:
            print("The given stock could not be found")
            return False
        return True

    def get_five_latest_days(self):
        self.get_data_from_api()
        # TODO: Get the date from the raw_data
        return_values = [{x, self.raw_data[x]["4. close"]} for x in self.raw_data]
        return return_values[:5]
