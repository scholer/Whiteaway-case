import random


class SalesCountRecommendationModel:

    def __init__(self, sales_df):
        # Først, lav en tabel med alle produkter.
        # OBS: Doing it this way makes 'StockCode' the table index, not a column:
        products_df = sales_df.groupby('StockCode').first()
        del products_df['InvoiceNo']
        del products_df['Quantity']
        del products_df['CustomerID']
        del products_df['Country']
        # self.products_df = products_df

        # Beregn product order count:
        # product_orders_count = df.groupby('StockCode')['InvoiceNo'].count().sort_values(ascending=False)
        products_df['OrdersCount'] = sales_df.groupby('StockCode')['InvoiceNo'].count()
        # Sort and store:
        self.products_df_sorted = products_df.sort_values(by='OrdersCount', ascending=False)

    def recommend_stockcodes(self, basket=None, k=1):
        """ This model doesn't use basket, only static sales numbers. """
        # display(self.products_df_sorted.index)
        return random.choices(
            self.products_df_sorted.index,
            weights=self.products_df_sorted['OrdersCount'],
            k=k
        )

    def recommend_product_row(self, basket=None):
        stockcode = self.recommend_stockcodes(basket=basket)[0]
        print(f"{stockcode!r}", type(stockcode))
        return self.products_df_sorted.loc[stockcode]
