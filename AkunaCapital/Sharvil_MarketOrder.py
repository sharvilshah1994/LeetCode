import ast


class AkunaMarketOrder:
    def __init__(self):
        self.buy_order = {}  # To maintain Buy orders. Eg: {Order_id: Quantity}
        self.sell_order = {}  # To maintain Sell orders. Eg: {Order_id: Quantity}
        self.cancel = []  # To maintain list of cancelled order ids
        self.order_mapping = {}  # To maintain Order mapping. Eg: {Order_id: Company_Symbol}
        self.position = {}  # To maintain marking. Eg: {Company_symbol: Marking}

    def on_event(self, s):
        dic = (ast.literal_eval(s))  # To convert String JSON to Python Dictionary
        side = ''
        if 'side' in dic:  # To check if 'side' key is in input JSON
            side = dic['side']
        type = dic['type']
        if 'symbol' in dic:
            self.order_mapping[dic['order_id']] = dic['symbol']
        if self.order_mapping[dic['order_id']] not in self.position:
            self.position[self.order_mapping[dic['order_id']]] = 0
        if type == 'NEW':  # To check if Order type is 'NEW'
            if side == 'BUY':  # Check if 'side' is 'BUY'
                self.buy_order[dic['order_id']] = dic['quantity']  # Adds Order_id and Quantity to 'buy_order' Dict
            elif side == 'SELL':  # Check if 'side' is 'SELL'
                self.position[dic['symbol']] -= dic['quantity']  # Subtract Sell quantity from the position
                self.sell_order[dic['order_id']] = dic['quantity']  # Add Order_id and Quantity to 'sell_order' Dict
        elif type == 'FILL':  # Check if type is 'FILL'
            if dic['remaining_quantity'] == 0:  # Check for remaining quantities to be filled
                if dic['order_id'] in self.buy_order:
                    self.position[self.order_mapping[dic['order_id']]] += self.buy_order[
                        dic['order_id']]  # If nothing remaining, update buy position
                    del self.buy_order[
                        dic['order_id']]  # Delete order id from buy_order dict if no remaining quantities
                elif dic['order_id'] in self.sell_order:
                    del self.sell_order[
                        dic['order_id']]  # Delete order id from sell_order dict if no remaining quantities
            else:
                if dic['order_id'] in self.buy_order:
                    self.position[self.order_mapping[dic['order_id']]] += dic['filled_quantity']
                    self.buy_order[dic['order_id']] = dic[
                        'remaining_quantity']  # Update buy dict with remaining quantities
                elif dic['order_id'] in self.sell_order:
                    self.sell_order[dic['order_id']] = dic[
                        'remaining_quantity']  # Update sell dict with remaining quantities
        elif type == 'ORDER_REJECT':  # Check if type is 'ORDER_REJECT'
            if dic['order_id'] in self.buy_order:  # If order_id in Buy_order dict and is not filled then
                # delete from Buy_order dict
                del self.buy_order[dic['order_id']]
            else:
                # Add to position if order is rejected
                self.position[self.order_mapping[dic['order_id']]] += self.sell_order[dic['order_id']]
                del self.sell_order[dic['order_id']]  # Delete from Sell_Order Dict
        elif type == 'CANCEL':  # Check if type is 'CANCEL'
            if (dic['order_id'] in self.buy_order) or (dic['order_id'] in self.sell_order):  # If order is in Buy_order
                # dict or Sell_order dict Add to cancelled list
                self.cancel.append(dic['order_id'])
        elif type == 'CANCEL_REJECT':  # Remove order id from the list if Cancel Reject is passed
            if (dic['order_id']) in self.cancel:
                self.cancel.remove(dic['order_id'])
        elif type == 'CANCEL_ACK':  # Check if type is 'CANCEL_ACK'
            if dic['order_id'] in self.cancel:  # If Order was cancelled before then add update position
                if dic['order_id'] in self.buy_order:
                    del self.buy_order[dic['order_id']]  # Since position not updates, just delete from buy_order dict
                else:
                    self.position[self.order_mapping[dic['order_id']]] += self.sell_order[
                        dic['order_id']]  # Update position
                    del self.sell_order[dic['order_id']]  # Delete from sell_order dict
        return self.position[self.order_mapping[dic['order_id']]]


s1 = '{"type": "NEW", "symbol": "AAPL", "order_id": 1, "side": "BUY", "quantity": 1700, "time": "2017-03-15T10:15:20.178562"}'
s21 = '{"type": "ORDER_ACK", "order_id": 1, "time": "2017-03-15T10:15:20.178725"}'
s2 = '{"type": "FILL", "order_id": 1, "filled_quantity": 1700, "remaining_quantity": 0, "time": "2017-03-15T10:15:20.178839"}'
s3 = '{"type": "NEW", "symbol": "AAPL", "order_id": 2, "side": "SELL", "quantity": 900, "time": "2017-03-15T10:15:20.178956"}'
s4 = '{"type": "CANCEL", "order_id": 2, "time": "2017-03-15T10:15:20.179069"}'
s5 = '{"type": "ORDER_ACK", "order_id": 2, "time": "2017-03-15T10:15:20.179166"}'
s6 = '{"type": "FILL", "order_id": 2, "filled_quantity": 900, "remaining_quantity": 0, "time": "2017-03-15T10:15:20.179271"}'
s7 = '{"type": "CANCEL_REJECT", "order_id": 2, "reason": "ORDER_ID_UNKNOWN", "time": "2017-03-15T10:15:20.179373"}'
s8 = '{"type": "NEW", "symbol": "MSFT", "order_id": 3, "side": "SELL", "quantity": 1900, "time": "2017-03-15T10:15:20.179572"}'
s9 = '{"type": "ORDER_ACK", "order_id": 3, "time": "2017-03-15T10:15:20.179848"}'
s10 = '{"type": "CANCEL", "order_id": 3, "time": "2017-03-15T10:15:20.179950"}'
s11 = '{"type": "CANCEL_ACK", "order_id": 3, "time": "2017-03-15T10:15:20.180047"}'
s12 = '{"type": "NEW", "symbol": "AAPL", "order_id": 4, "side": "SELL", "quantity": 600, "time": "2017-03-15T10:15:20.180214"}'
s13 = '{"type": "ORDER_ACK", "order_id": 4, "time": "2017-03-15T10:15:20.180319"}'
s14 = '{"type": "CANCEL", "order_id": 4, "time": "2017-03-15T10:15:20.180406"}'
s15 = '{"type": "CANCEL_REJECT", "order_id": 4, "reason": "", "time": "2017-03-15T10:15:20.180505"}'
s16 = '{"type": "NEW", "symbol": "MSFT", "order_id": 5, "side": "SELL", "quantity": 2000, "time": "2017-03-15T10:15:20.180679"}'
s17 = '{"type": "ORDER_REJECT", "order_id": 5, "reason": "FIRM_RISK_LIMIT_EXCEEDED", "time": "2017-03-15T10:15:20.180825"}'
s18 = '{"type": "NEW", "symbol": "SPY", "order_id": 6, "side": "BUY", "quantity": 200, "time": "2017-03-15T10:15:20.180958"}'
s19 = '{"type": "ORDER_ACK", "order_id": 6, "time": "2017-03-15T10:15:20.181062"}'
s20 = '{"type": "FILL", "order_id": 6, "filled_quantity": 60, "remaining_quantity": 140, "time": "2017-03-15T10:15:20.181170"}'

c = AkunaMarketOrder()
print(c.on_event(s1))
print(c.on_event(s21))
print(c.on_event(s2))
print(c.on_event(s3))
print(c.on_event(s4))
print(c.on_event(s5))
print(c.on_event(s6))
print(c.on_event(s7))
print(c.on_event(s8))
print(c.on_event(s9))
print(c.on_event(s10))
print(c.on_event(s11))
print(c.on_event(s12))
print(c.on_event(s13))
print(c.on_event(s14))
print(c.on_event(s15))
print(c.on_event(s16))
print(c.on_event(s17))
print(c.on_event(s18))
print(c.on_event(s19))
print(c.on_event(s20))
