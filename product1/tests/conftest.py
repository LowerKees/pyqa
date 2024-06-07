"""Shared fixtures across all product1 tests."""

from typing import Generator

import pytest
from delta import configure_spark_with_delta_pip
from pyspark.sql import DataFrame, SparkSession


@pytest.fixture
def spark_session() -> Generator[SparkSession, None, None]:
    """Single spark session per test session."""
    builder = (
        SparkSession.builder.appName("test_1")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    yield spark


@pytest.fixture
def dummy_data_frame(spark_session) -> Generator[DataFrame, None, None]:
    """Data frame that can be used for simple test cases."""
    data = [[1, "first_row"], [2, "second_row"]]
    schema = "id INT, label STRING"

    df = spark_session.createDataFrame(data=data, schema=schema)
    yield df
