# %%

import pandas as pd
from collections import Counter
from utils import download_pdf
from tqdm import tqdm

# %%
"""
df=pd.read_csv("data/cc-hosts-20230303.csv")
ja_df=df[df["tld"]=="jp"]
ja_df=ja_df[ja_df["file_name"]==ja_df["file_name"]]
ja_df = ja_df.drop_duplicates(subset=['file_name'])

ja_df.to_csv("ja_df.csv")
"""

# %%
target_df = pd.read_csv("ja_df.csv")

# %%
# target_host=".ac"
# target_df=ja_df[ja_df["host"].str.find(target_host)>0]
print(target_df.shape)
file_name_list = list(target_df["file_name"])

zip_index_list = [i[:4] for i in file_name_list]

counts = Counter(zip_index_list)
sorted_counts = counts.most_common()
download_zip_order = [i[0] for i in sorted_counts if i[1] > 0]
download_zip_order

# %%


# %%
for target_zip_id in tqdm(download_zip_order):
    print("start ", target_zip_id)
    download_pdf(target_zip_id, file_name_list)
