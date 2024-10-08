from l0_ingest_from_source.graph.TableIterator.config.Config import SubgraphConfig as TableIterator_Config
from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, TableIterator: dict=None, catalog_name: str=None, schema_name: str=None, **kwargs):
        self.spark = None
        self.update(TableIterator, catalog_name, schema_name)

    def update(self, TableIterator: dict={}, catalog_name: str="ntong", schema_name: str="default", **kwargs):
        prophecy_spark = self.spark
        self.TableIterator = self.get_config_object(
            prophecy_spark, 
            TableIterator_Config(prophecy_spark = prophecy_spark), 
            TableIterator, 
            TableIterator_Config
        )
        self.catalog_name = catalog_name
        self.schema_name = schema_name
        pass
