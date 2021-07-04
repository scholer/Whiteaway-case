import pandas as pd

from collections import defaultdict
import timeit
import itertools
import random
import matplotlib
from matplotlib import pyplot


def build_sameorder_product_dod_using_cartesian_forloop(df):
    # We use a double default-dict, but since most StockCodes are present,
    # it is probably faster to pre-populate the outer dict with *all* StockCodes.
    # Also, we only have 3684, so it would be possible to use an adjacency matrix,
    # instead of adjacency list - only about 10M values so about 40-80 MB.

    sameorder_dod = defaultdict(lambda: defaultdict(int))
    for invoiceno, order_df in df.groupby("InvoiceNo"):
        # Can use either itertools.product or itertools.combinations:
        # itertools.combinations only gives unique combinations, but can do more than two.
        for stock_code1, stock_code2 in itertools.product(order_df['StockCode'], repeat=2):
            if stock_code1 == stock_code2:
                continue
            sameorder_dod[stock_code1][stock_code2] += 1
    return sameorder_dod


class SameOrderGraphRecommender:

    def __init__(self, sales_df):

        # Build same-order undirected graph:
        # dict[StockCode1][StockCode2] = count
        print("Dataset:")
        print(f"- {len(df)} rows,")
        print(f"- {df.groupby('InvoiceNo').ngroups} orders/invoices,")
        print(f"- {len(df['StockCode'].unique())} unique StockCodes.")

        print("Building SameOrder graph (dict-of-dict)... This should take about 5-10 seconds.")
        t1 = timeit.default_timer()
        self.sameorder_dod = build_sameorder_product_dod_using_cartesian_forloop(sales_df)
        ttc = timeit.default_timer() - t1
        print(f" - Done ({ttc:.2f} s).")

    def recommend_stockcodes(self, basket, k=1):
        if isinstance(basket, str):
            basket = [basket]
        item_weights = defaultdict(int)
        for item in basket:
            # self.sameorder_dod[item] = {stockcode: weight}
            for stockcode, count in self.sameorder_dod[item].items():
                item_weights[stockcode] += count
        codes, weights = zip(*item_weights.items())
        return random.choices(codes, weights=weights, k=k)

    def recommend_top_stockcodes(self, basket, k=1):
        if isinstance(basket, str):
            basket = [basket]
        item_weights = defaultdict(int)
        for item in basket:
            # data structure is: self.sameorder_dod[item] = {stockcode: weight}
            if item not in self.sameorder_dod:
                print(f"NOTICE: Item stockcode {item} not present in SameOrder graph.")
                print(f"Perhaps the item has never been bought together with other items?")
            for stockcode, count in self.sameorder_dod[item].items():
                item_weights[stockcode] += count
        item_weights = dict(item_weights)
        codes, weights = zip(*item_weights.items())
        codes, weights = np.array(codes), np.array(weights)
        sidxs = np.argsort(weights)
        codes = codes[sidxs]
        return codes[:k]
