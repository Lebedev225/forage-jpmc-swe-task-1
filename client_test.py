import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(
                quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(
                quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        ratio = getRatio(prices["ABC"], prices["DEF"])
        self.assertEqual(ratio, ((quotes[0]['top_bid']['price'] + quotes[0]['top_ask']
                                  ['price'])/2)/((quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price'])/2))

    def test_getRatio_calculatePriceAZero(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        ratio = getRatio(prices["ABC"], prices["DEF"])
        self.assertEqual(ratio, 0)

    def test_getRatio_calculatePriceBZero(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price

        ratio = getRatio(prices["ABC"], prices["DEF"])
        self.assertEqual(ratio, 0)


if __name__ == '__main__':
    unittest.main()
