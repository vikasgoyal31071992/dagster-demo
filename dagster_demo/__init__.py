
# from dagster import Definitions, load_assets_from_modules

# from .assets import mongodb
# from dagster_embedded_elt.dlt import DagsterDltResource


# mongo_assets = load_assets_from_modules([mongodb])

# defs = Definitions(
#     assets = [*mongo_assets],
#     resources = {
#         "dlt": DagsterDltResource()
#     }
# )