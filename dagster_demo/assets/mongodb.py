import dlt
from ..mongodb import mongodb

from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets

movies = mongodb(
    database='sample_mflix'
).with_resources(
    "comments",
    "embedded_movies",
    "movies",
    "sessions",
    "theaters",
    "users"
)

@dlt_assets(
    dlt_source=movies,
    dlt_pipeline=dlt.pipeline(
        pipeline_name="local_mongo",
        destination='snowflake',
        dataset_name="mflix",
    ),
    name="mongodb",
    group_name="mongodb",
)
def dlt_asset_factory(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context, write_disposition="merge")