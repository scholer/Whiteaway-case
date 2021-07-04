# Copyright 2021, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

This recommender simply recommends things that the user have previously purchased.

Can be optimized for consumables, i.e. products that the customer, or other customers,
have previously purchased more than one off.


(There is probably a distinct difference between products that a user purchases only once,
and products that are being purchased repeatedly.)


"""
import random


class BuyItAgainRecommender:

    def __init__(self, sales_df):
        # Approach:
        # 1. Group by user.
        # 2. For each user, count how many times that user has bought a given product.
        # 3. Recommend the products that the user has purchased the most (maybe as a weight for random choice).
        # 4. Maybe filter out non-consumable products so we mostly recommend consumable products
        #    that the customer is actually likely to buy multiple of.

        # df_gby_customerid = sales_df.groupby('CustomerID')

        # You cannot do `sales_df.groupby('CustomerID').groupby('StockCode')`
        # To group multiple times, provide a list of columns:
        # self.user_product_count = sales_df.groupby(['CustomerID', 'StockCode']).size()
        # Use agg to count the number of orders of each product (for each user):
        # (we could consider summing the quantity here)
        # self.user_product_count = sales_df.groupby('CustomerID').agg({'StockCode': 'size'})
        # This form allows us to rename the output column (pocount = purchase order count):
        self.customer_product_count = sales_df.groupby(['CustomerID', 'StockCode']).agg(pocount=('StockCode', 'size'))

        # We only have a single-column dataframe (with a multi-index), so we could consider converting to series.

    def recommend_stockcodes(self, k=1, customerid=None, basket=None):
        """ Recommend `k` number of products (StockCodes).
        This model doesn't use basket, only static sales numbers,
        but `basket` is in the API for consistency between recommender models.
        """
        assert customerid
        customer_product_pocount = self.customer_product_count.loc[customerid]
        # Note: Random picks, with replacement (so same item can be present multiple times).
        return random.choices(
            customer_product_pocount.index,
            weights=customer_product_pocount['pocount'],
            k=k
        )

    def recommend_top_stockcodes(self, k=1, customerid=None, basket=None):
        """ Recommend `k` number of products (StockCodes).
        This is a non-random version, which will always just return the top candidates.
        This model doesn't use basket, only static sales numbers,
        but `basket` is in the API for consistency between recommender models.
        """
        assert customerid
        return self.customer_product_count.loc[customerid]['pocount'].sort_values(ascending=False).iloc[:k].index


