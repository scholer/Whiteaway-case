

def build_products_df_from_sales(sales_df):
    """ Build a table with products based on the sales table.
    It groups by stock code and takes the first row in each group,
    then removes sales-specific columns (invoice, quantity, customerid, country).
    This also calculates the total number of orders for a given product, "OrdersCount",
    as well as how many distinct users has purchased a given product, "UsersCount",
    and adds these as columns to the product table.
    """

    # Først, lav en tabel med alle produkter.
    products_df = sales_df.groupby('StockCode').first()
    del products_df['InvoiceNo']
    del products_df['Quantity']
    del products_df['CustomerID']
    del products_df['Country']

    # Beregn product order count:
    product_orders_count = sales_df.groupby('StockCode').size()
    products_df['OrdersCount'] = product_orders_count

    # Beregn hvor mange brugere har købt hvert enkelt produkt:
    products_df['UsersCount'] = product_users_count = sales_df.groupby('StockCode')['CustomerID'].nunique()

    return products_df
