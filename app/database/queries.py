from datetime import datetime as dt

from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from database.models import HeartRateOrm, UserOrm


class UserQueries:
    def __init__(self, session: Session):
        self.session = session

    def query_users(self, min_age: int, gender: str, min_avg_heart_rate: float, date_from: dt, date_to: dt):
        """
        Returns all users who are older than min_age and have an average heart rate
        higher than min_avg_heart_rate within a specified time range.

        :param min_age: Minimum age of users
        :param gender: Gender of users
        :param min_avg_heart_rate: Minimum average heart rate
        :param date_from: Start of the time range
        :param date_to: End of the time range
        :return: List of users meeting the criteria
        """
        subquery = (
            self.session.query(
                HeartRateOrm.user_id,
                func.avg(HeartRateOrm.heart_rate).label("avg_heart_rate"),
            )
            .filter(
                HeartRateOrm.timestamp >= date_from,
                HeartRateOrm.timestamp <= date_to,
            )
            .group_by(HeartRateOrm.user_id)
            .subquery()
        )

        query = (
            self.session.query(UserOrm)
            .join(subquery, UserOrm.id == subquery.c.user_id)
            .filter(
                UserOrm.age > min_age,
                UserOrm.gender == gender,
                subquery.c.avg_heart_rate > min_avg_heart_rate,
            )
        )

        return query.all()

    def query_for_user(self, user_id: int, date_from: dt, date_to: dt):
        """
        Returns the top 10 highest average heart rate values
        for hourly intervals within the specified date range.

        :param user_id: ID of the user
        :param date_from: Start of the time range
        :param date_to: End of the time range
        :return: List of tuples (HeartRateOrm, hour, average heart rate)
        """
        query = (
            self.session.query(
                extract("hour", HeartRateOrm.timestamp).label("hour"),
                func.avg(HeartRateOrm.heart_rate).label("avg_heart_rate_by_hour"),
            )
            .filter(
                HeartRateOrm.user_id == user_id,
                HeartRateOrm.timestamp >= date_from,
                HeartRateOrm.timestamp <= date_to,
            )
            .group_by(extract("hour", HeartRateOrm.timestamp))
            .order_by(func.avg(HeartRateOrm.heart_rate).desc())
            .limit(10)
        )

        return query.all()
