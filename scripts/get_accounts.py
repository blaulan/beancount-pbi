import pandas as pd
from beancount.query import query
from beancount import loader

input_file = dataset['data_path'][0]
query_str = """
SELECT DISTINCT
    account,
    getitem(open_meta(account), "asset-type") AS asset_type,
    getitem(open_meta(account), "mortage-id") AS mortage_id,
    getitem(open_meta(account), "interest-rate") AS interest_rate
ORDER BY account
""".strip()

_entries, _errors, _options_map = loader.load_file(input_file)
output = query.run_query(_entries, _options_map, query_str)
records = pd.DataFrame(output[1])

print(records)
