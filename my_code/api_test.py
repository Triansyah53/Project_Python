import pprint

from woocommerce import API

wcapi = API(
    url="http://mystore.local/",
    consumer_key="ck_16581c7ecdceacada4fbd90eff1ae185482edcf9",
    consumer_secret="cs_4e0b376a9d180fb2d8862387a1aae73df92827a8",
    version="wc/v3"
)

r = wcapi.get("products")
pp=pprint.PrettyPrinter()
pp.pprint(r.json())