import os
from functools import cache

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Organisation


@cache
def engine():
    return create_engine(os.environ["DATABASE_URL"])


def find_organisations():
    engine_builder = engine()
    with Session(engine_builder) as session:
        query = select(Organisation).filter_by(id="BOR")
        results = session.execute(query)
        for result in results:
            print(result)