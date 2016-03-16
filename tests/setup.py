# -*- coding: utf-8 -*-

import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    file_name = os.path.abspath(sys.argv[0])
    path = os.path.dirname(file_name)
    project_path = os.path.dirname(path)
    sys.path.append(project_path)
    from web import mysql_test_url, db

    engine = create_engine(mysql_test_url)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    sql_script = os.path.join(project_path, "scripts/schema.sql")

    with open(sql_script) as f:
        content = f.read()
    sql = 'DROP DATABASE IF EXISTS falcon_portal_test; CREATE DATABASE falcon_portal_test; ' \
          'USE falcon_portal_test'
    session.execute(sql)
    session.execute(content)

if __name__ == '__main__':
    main()
