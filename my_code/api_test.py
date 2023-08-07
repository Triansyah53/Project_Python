import pprint

from woocommerce import API

wcapi = API(
    url="http://mystore.local/",
    consumer_key="ck_9a8d25d9727c105ccce0c7d13178f058bbd39a6d",
    consumer_secret="cs_1e16ff2b740969b57a792b0fc15fc79590ba55b3",
    version="wc/v3"
)

r = wcapi.get("products")
pp=pprint.PrettyPrinter()
pp.pprint(r.json())