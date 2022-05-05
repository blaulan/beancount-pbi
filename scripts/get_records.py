import pandas as pd
from beancount.query import query
from beancount import loader

input_file = dataset['data_path'][0]
query_str = """
SELECT
    id, date, type, payee, account,
    units(position) AS units_position,
    convert(cost(position), '{currency}') AS cost_position,
    convert(value(position), '{currency}') AS value_position,
    narration, links, tags
""".strip().format(currency=dataset['currency'][0])

_entries, _errors, _options_map = loader.load_file(input_file)
output = query.run_query(_entries, _options_map, query_str)
records = pd.DataFrame(output[1])
records['links'] = records['links'].apply(','.join)
records['tags'] = records['tags'].apply(','.join)

print(records)
