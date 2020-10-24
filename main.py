import API.AlphaVantageConnection as data


def main():
    time_series = data.StockTimeSeries(symbol='MSFT')
    endpoint = data.Endpoint()
    print(endpoint.search_endpoint('rolls'))


if __name__ == '__main__':
    main()
