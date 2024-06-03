import logging

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from config import settings
from database.models import Base


class Database:
    def __init__(self, database_url: str):
        """
        Initialize the Database class with a given database URL.

        :param database_url: URL of the database to connect to.
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.engine = create_engine(database_url)
        self.session = sessionmaker(bind=self.engine)

    def create_tables(self) -> None:
        """
        Create all tables defined in the Base metadata.
        Logs success or any SQLAlchemy errors encountered.
        """
        try:
            Base.metadata.create_all(bind=self.engine)
            self.logger.info("Tables created successfully.")
        except SQLAlchemyError as e:
            self.logger.error(f"Error creating tables: {e}")

    def get_session(self):
        """
        Get a session.

        :return: A session object.
        """
        try:
            return self.session()
        except SQLAlchemyError as e:
            self.logger.error(f"Error getting session: {e}")
            raise


DATABASE_URL = settings.db_url
db = Database(DATABASE_URL)
