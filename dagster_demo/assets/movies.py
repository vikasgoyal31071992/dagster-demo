from dagster_snowflake import SnowflakeResource
from dagster import asset

import os
import pandas as pd


@asset(
        deps=['dlt_mongodb_comments','dlt_mongodb_embedded_movies']
)
def user_engagement(snowflake: SnowflakeResource) -> None:
    
    """
    Movie titles and the number of user engagement (i.e. comments)
    """
    query = """
        select
            movies.title,
            movies.year AS year_released,
            count(*) as number_of_comments
        from comments comments
        join embedded_movies movies on comments.movie_id = movies._id
        group by movies.title, movies.year
        order by number_of_comments desc
    """
    with snowflake.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        engagement_df = cursor.fetch_pandas_all()

    engagement_df.to_csv('data/movie_engagement.csv', index=False)

@asset(
    deps=["dlt_mongodb_embedded_movies"]
)
def top_movies_by_month(context, snowflake: SnowflakeResource) -> None:
    pass

@asset(
    deps=["user_engagement"]
)
def top_movies_by_engagement():
    
    df = pd.read_csv('data/movie_engagement.csv')