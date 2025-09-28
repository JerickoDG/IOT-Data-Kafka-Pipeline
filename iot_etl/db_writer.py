from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Base, IOTData

class MySQLWriter:
    def __init__(self, config: dict):
        url = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        self.engine = create_engine(url, echo=False, pool_recycle=600)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def write(self, data: dict):
        session = self.Session()
        try:
            row = IOTData(**data)
            session.add(row)
            session.commit()
            print(f"[MYSQLWriter] Inserted record for {data['created_at']}")
        except IntegrityError:
            # This happens if created_at already exists due to the UNIQUE constraint
            session.rollback()
            print(f"[MYSQLWriter] Record for {data['created_at']} already exists. Skipping insert.")
        except Exception as e:
            session.rollback()
            print(f"[MYSQLWriter] Error writing to database: {e}")
        finally:
            session.close()