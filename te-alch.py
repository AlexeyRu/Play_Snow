import json
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import argparse

def get_credits():
    # get user credits from json-file for connecting to database

    f = open('C:/Users/rudnikevich/PycharmProjects/Test/venv/snowflake_creds.json', 'r')
    ff = json.loads(f.read())
    print(ff)
    f.close()
    return ff

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('num_in_request', metavar='N', type=int,
                        help='row number in request')
    args = parser.parse_args()

    print("!!!", args.num_in_request)

    cred = get_credits()

    engine = create_engine(
        'snowflake://{user}:{password}@{account}/'.format(
            user=cred['user'],
            password=cred['password'],
            account=cred['account'],
        )
    )
    try:
        connection = engine.connect()

        sql_text = "SELECT b.PRODUCTCODEHASH , b.NAME , h.PRODUCTCODE " \
                   "FROM  DATAVAULT_LDA_91.SAT_PRODUCTCODE b " \
                   "INNER JOIN  DATAVAULT_LDA_91.HUB_PRODUCTCODE h ON h.PRODUCTCODEHASH = b.PRODUCTCODEHASH " \
                   "where b.NAME is not NULL " \
                   "LIMIT "+str(args.num_in_request)

        results = connection.execute(sql_text).fetchall()

        print(results[0],len(results))

        df = pd.read_sql_query(sql_text, engine)
        print(type(df))
        print(df.head())

        print('\nVersion number one:\n',df.to_json())
        print('\nVersion number two:\n',df.to_json(orient='records'))

    finally:
        connection.close()
        engine.dispose()

if __name__ == '__main__':
    main()