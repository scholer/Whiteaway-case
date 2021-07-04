# Copyright 2021, Rasmus Sorensen <rasmusscholer@gmail.com>
"""


"""

import pandas as pd

from src.models.buyitagain_recommender import BuyItAgainRecommender
from src.data.data_filtering import load_and_filter

INPUT_FILE = "data/raw/data.csv"


def test_buyitagain_01():
    # Load data
    df = load_and_filter(INPUT_FILE)

    recommender = BuyItAgainRecommender(sales_df=df)

    # This user has many purchases, 103 products in 182 orders.
    cid = '12347'
    top5_picks = recommender.recommend_top_stockcodes(k=5, customerid=cid)
    print(top5_picks)
    assert len(top5_picks) == 5
    assert list(top5_picks) == ['22375', '21731', '84558A', '22727', '22423']
    assert (top5_picks == ['22375', '21731', '84558A', '22727', '22423']).all()  # alternatively

    random7_picks = recommender.recommend_stockcodes(k=7, customerid=cid)
    assert len(random7_picks) == 7

    # What about a user who only has a few product orders?
    # This user has two orders, each order for the same single product 23166 "MEDIUM CERAMIC TOP STORAGE JAR"
    cid = '12346'
    random7_picks = recommender.recommend_stockcodes(k=7, customerid=cid)
    assert len(random7_picks) == 1
    assert list(random7_picks) == ['23166']




