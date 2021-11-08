from pushover import Client


def notify(message, title):
    # Notification to my device (please here change the token to yours pushover token)
    client = Client("ua8hh7y8923wxhax5ofws8113ejafb", api_token="a4w5z5mt382yzrjrq2nrbnt57fcjao")
    client.send_message(message, title)
