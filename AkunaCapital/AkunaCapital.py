import json


class OrderMarking:
    def __init__(self):
        self.marking = 0
        self.buy_orders = dict()
        self.sell_orders = dict()

    def on_event(self, event):
        event = json.loads(event)
        type = event['type']

        events = {"NEW": self.new_event,
                  "ORDER_REJECT": self.order_reject,
                  "FILL": self.fill,
                  "CANCEL_ACK": self.cancel_ack}

        if type in events:
            events[type](event)
        return self.marking

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
        self.marking -= int(event['quantity'])

    def order_reject(self, event):
        order_id = event['order_id']
        if order_id in self.sell_orders:
            self.marking += int(self.sell_orders[order_id])
            del self.sell_orders[order_id]
        elif order_id in self.buy_orders:
            del self.buy_orders[order_id]

    def fill(self, event):
        order_id = event['order_id']
        filled_quantity = int(event['filled_quantity'])
        remaining_quantity = int(event['remaining_quantity'])
        if order_id in self.buy_orders:
            self.buy_orders[order_id] -= filled_quantity
            if self.buy_orders[order_id] < 0 or remaining_quantity == 0:
                del self.buy_orders[order_id]
            self.marking += filled_quantity
        elif order_id in self.sell_orders:
            self.sell_orders[order_id] -= filled_quantity
            if self.sell_orders[order_id] < 0 or remaining_quantity == 0:
                del self.sell_orders[order_id]

    def cancel_ack(self, event):
        order_id = event['order_id']
        if order_id in self.sell_orders:
            self.marking += int(self.sell_orders[order_id])
            del self.sell_orders[order_id]
        elif order_id in self.buy_orders:
            del self.buy_orders[order_id]


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
