from API.YahooFinance import StockTimeSeries


class FinancialActions:
    @staticmethod
    def buy(ticker, number):
        data = StockTimeSeries().historical_data(ticker,'1d','1d')
        price = float(data.Open[0])
        return price*number

    @staticmethod
    def sell(ticker, number):
        data = StockTimeSeries().historical_data(ticker, '1d', '1d')
        price = float(data.Open[0])
        brokerage_fee = 0.1
        return price*number*(1-brokerage_fee)
