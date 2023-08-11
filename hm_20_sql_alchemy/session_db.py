from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("mysql+mysqlconnector://root:1qazxsw2@localhost/hm_20_store")

__session = sessionmaker(engine)

session: Session = __session()
