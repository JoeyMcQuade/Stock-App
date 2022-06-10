from get_stock_data import StockData


def gui():
    return StockData().get_five_latest_days()


if __name__ == "__main__":
    print(gui())
