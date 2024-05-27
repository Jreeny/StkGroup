from tabulate import tabulate

table_header = ['name', '语文', '数学', '英语']
table_data = [
    ('李卓', '90', '80', '85'),
    ('Jim', '70', '90', '80'),
    ('Lucy', '90', '70', '90'),
]


print(tabulate(table_data, headers=table_header, tablefmt='pretty'))