import agate

table=agate.Table.from_csv('most-medals-won.csv')
table.to_json('most-medals-won.json')
