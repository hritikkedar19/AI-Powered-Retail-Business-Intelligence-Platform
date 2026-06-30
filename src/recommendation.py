import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

def build_recommendations(df, products):
    basket = pd.crosstab(df['customer_id'], df['product_name'])
    similarity = cosine_similarity(basket.T)
    sim_df = pd.DataFrame(similarity, index=basket.columns, columns=basket.columns)
    recs = []
    for product in sim_df.index:
        top = sim_df[product].sort_values(ascending=False).iloc[1:6]
        recs.append({'product_name': product, 'recommended_products': ', '.join(top.index)})
    rec_df = pd.DataFrame(recs)
    rec_df.to_csv(OUT / 'product_recommendations.csv', index=False)
    return rec_df
