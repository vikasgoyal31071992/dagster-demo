
from dagster import Definitions, load_assets_from_modules, EnvVar

from .assets import mongodb, movies
from dagster_embedded_elt.dlt import DagsterDltResource
from dagster_snowflake import SnowflakeResource


mongo_assets = load_assets_from_modules([mongodb])
movies_assets = load_assets_from_modules([movies], group_name="movies")

snowflake = SnowflakeResource(
    account = "XXX",
    user = "XXX",
    password = "XXX",
    database = "dagster_db",
    warehouse = "dagster_wh",
    role = "dagster_role",
)

defs = Definitions(
    assets = [*mongo_assets, *movies_assets],
    resources = {
        "dlt": DagsterDltResource(),
        "snowflake": snowflake,
    }
)