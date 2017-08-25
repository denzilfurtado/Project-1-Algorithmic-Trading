from fmclient import Agent
from fmclient import Order, OrderType, OrderSide, Holding
import copy


class FMBot(Agent):
    """
    This is a very simple "Hello World" agent!
    """
    def __init__(self, account, email, password, marketplace_id):
        name = "Knight Of The Eastern Calculus"
        super().__init__(account, email, password, marketplace_id,
                         name=name)
        self.description = " Hello bot2!"

    def initialised(self):
        for market_id, market_info in self.markets.items():
            market_item = market_info["item"]
            print("I can trade " + str(market_item) +" by sending orders with market id " + str(market_id))

    def received_order_book(self, order_book, market_id):
        for order in order_book:
            if order.mine:
                print("This is my order!")

    def received_holdings(self, holdings):
        cash_holdings = holdings["cash"]
        print("Total cash: " + str(cash_holdings["cash"]) +" available cash: " + str(cash_holdings["available_cash"]))
        for market_id, market_holding in holdings["markets"].items():
            print("Market " + str(market_id) + " total units: " +str(market_holding["units"]) + ", available units: " +str(market_holding["available_units"]))

    def received_marketplace_info(self, marketplace_info):
        (market_id , market_info) = self.markets.items()
        if marketplace_info["status"]:
            print("Marketplace is now open with session id " + str(session_id), True)
        else:
            print("Marketplace is now closed.", True)

    def received_completed_orders(self, orders, market_id=None):
        pass
        

    def order_accepted(self, order):
        pass

    def order_rejected(self, info, order):
        pass

    def run(self):
        try:
            self.initialise()
            self.initialised ()    
            self._get_marketplace_info()
            print (self._markets_url)
            print (self._session_url)
            print (self._holdings_url)
            self.start()
        except:
            print ("caught something")

if __name__ == "__main__":
    marketplace_id = 72
    fm_bot = FMBot("durable-guard", "f.aijaz@student.unimelb.edu.au", "flavleCh", marketplace_id)
    fm_bot.run()
    