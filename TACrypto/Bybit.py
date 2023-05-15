# Import pybit and define the HTTP object.

"""
Some methods might need extra arguments due to the current Bybit APIs -
which are divided across market types. To ensure you're sending requests to
a specific market type, like Inverse Perpetual, you can import and define
HTTP like so:
from pybit.inverse_perpetual import HTTP   <-- exclusively supports spot.
"""

from pybit import HTTP  # supports inverse perp futures, usdt perp, spot.
from pybit import inverse_perpetual  # <-- import HTTP & WSS for inverse perp

from pybit import spot  # <-- import HTTP & WSS for spot

"""
You can create an authenticated or unauthenticated HTTP session. 
You can skip authentication by not passing any value for the key and secret.
"""

# Unauthenticated
session_unauth = inverse_perpetual.HTTP(endpoint="https://api.bybit.com")



# Let's get market information about EOSUSD. Note that "symbol" is
# a required parameter as per the Bybit API documentation.
session_unauth.latest_information_for_symbol(symbol="EOSUSD")

