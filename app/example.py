import datetime

from database.database import db
from database.queries import UserQueries


def main():
    db.create_tables()
    session = db.get_session()

    min_age = 25
    gender = 'Female'
    min_avg_heart_rate = 120
    date_from = datetime.datetime(2023, 1, 1)
    date_to = datetime.datetime(2023, 12, 31)

    user_queries = UserQueries(session)

    users_result = user_queries.query_users(min_age, gender, min_avg_heart_rate, date_from, date_to)
    for user in users_result:
        print(user.name, user.age, user.gender)

    user_id = 1
    heart_rate_result = user_queries.query_for_user(user_id, date_from, date_to)
    for record in heart_rate_result:
        print(record.hour, record.avg_heart_rate_by_hour)


if __name__ == "__main__":
    main()
