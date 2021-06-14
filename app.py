import sys
from config import DB_DETAILS
from util import get_tables, load_db_details
from read import read_table


def main():
    """"Program atleast take 1 argument"""
    env = sys.argv[1]
    # db_details = DB_DETAILS[env]
    db_details = load_db_details(env)
    tables = get_tables('table_list')
    for table_name in tables['table_name']:
        print(f'reading data for {table_name}')
        data, column_name = read_table(db_details, tables)
        print(f'reading data for {table_name}')
    for rec in data:
        print(rec)






if __name__ == '__main__':
    main()
