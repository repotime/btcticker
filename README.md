# Btcticker
A Bitcoin price ticker that grabs the current Bitcoin price from Coingecko's API and displays it every X seconds.

#Caution
You may at some point be rate limited by Coingecko's API, keep the request time to 10 seconds or over to not max out the API requests.

At times the price may look like its not updating, don't worry as this is not a bug. The price movements may be so shallow that the API won't update the call, you can really notice this during off-peak trading hours.
