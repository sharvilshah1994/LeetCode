import json


class OrderMarking:
    def __init__(self):
        self.buy_orders = dict()
        self.sell_orders = dict()
        self.cancel = list()
        self.order_mapping = dict()
        self.position = dict()

    def on_event(self, event):
        event = json.loads(event)
        type = event['type']
        events = {"NEW": self.new_event,
                  "ORDER_REJECT": self.order_reject,
                  "FILL": self.fill,
                  "CANCEL_ACK": self.cancel_ack,
                  "CANCEL": self.cancel_event,
                  "CANCEL_REJECT": self.cancel_reject }
        if 'symbol' in event:
            self.order_mapping[event['order_id']] = event['symbol']
        if self.order_mapping[event['order_id']] not in self.position:
            self.position[self.order_mapping[event['order_id']]] = 0
        if type in events:
            events[type](event)
        return self.position[self.order_mapping[event['order_id']]]

    def new_event(self, event):
        side = event['side']
        if side == "BUY":
            self.buy_order(event)
        elif side == "SELL":
            self.sell_order(event)

    def buy_order(self, event):
        self.buy_orders[event['order_id']] = int(event['quantity'])

    def sell_order(self, event):
        self.sell_orders[event['order_id']] = event['quantity']
        self.position[event['symbol']] -= event['quantity']

    def order_reject(self, event):
        order_id = event['order_id']
        if order_id in self.sell_orders:
            self.position[self.order_mapping[event['order_id']]] += self.sell_order[event['order_id']]
            del self.sell_orders[order_id]
        elif order_id in self.buy_orders:
            del self.buy_orders[order_id]

    def fill(self, event):
        order_id = event['order_id']
        filled_quantity = int(event['filled_quantity'])
        remaining_quantity = int(event['remaining_quantity'])
        if remaining_quantity == 0:
            if order_id in self.buy_orders:
                self.position[self.order_mapping[order_id]] += self.buy_orders[order_id]
                del self.buy_orders[order_id]
            elif event['order_id'] in self.sell_order:
                del self.sell_orders[order_id]
        else:
            if event['order_id'] in self.buy_orders:
                self.position[self.order_mapping[order_id]] += filled_quantity
                self.buy_orders[order_id] = remaining_quantity
            elif order_id in self.sell_orders:
                self.sell_orders[order_id] = remaining_quantity

    def cancel_ack(self, event):
        order_id = event['order_id']
        if order_id in self.cancel:
            if order_id in self.buy_orders:
                del self.buy_orders[order_id]
            else:
                self.position[self.order_mapping[order_id]] += int(self.sell_orders[order_id])
                del self.sell_orders[order_id]

    def cancel_event(self, event):
        order_id = event['order_id']
        if (order_id in self.buy_orders) or (order_id in self.sell_orders):
            self.cancel.append(order_id)

    def cancel_reject(self, event):
        order_id = event['order_id']
        if order_id in self.cancel:
            self.cancel.remove(order_id)


order = OrderMarking()
events = [
    '{"type":"NEW", "order_id":"1", "side":"SELL", "quantity":"900"}',
    '{"type":"ORDER_ACK", "order_id":"1"}',
    '{"type":"CANCEL", "order_id":"1"}',
    '{"type":"CANCEL_ACK", "order_id":"1"}',
    '{"type":"NEW", "order_id":"2", "side":"BUY", "quantity":"400"}',
    '{"type":"ORDER_REJECT", "order_id":"2"}',
    '{"type":"NEW", "order_id":"3", "side":"BUY", "quantity":"1800"}',
    '{"type":"ORDER_ACK", "order_id":"3"}',
    '{"type":"FILL", "order_id":"3", "filled_quantity":1100, "remaining_quantity":700}',
    '{"type":"NEW", "order_id":"4", "side":"SELL", "quantity":"1100"}',
    '{"type":"ORDER_REJECT", "order_id":"4"}',
    '{"type":"CANCEL", "order_id":"3"}',
    '{"type":"CANCEL_ACK", "order_id":"3"}',
    '{"type":"FILL", "order_id":"3", "filled_quantity":700, "remaining_quantity":0}'
]

for e in events:
    print(order.on_event(e))
