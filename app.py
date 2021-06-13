import sys
from config import DB_DETAILS


def main():
    """"Program atleast take 1 argument"""
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)



if __name__ == '__main__':
    main()
