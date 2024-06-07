# ruff: noqa: D103
"""Tests product1.processor objects."""

import datetime
from typing import Generator

import pytest
from pyspark.sql import DataFrame
from pyspark.testing.utils import assertDataFrameEqual

from product1.processor import add_creation_dts


@pytest.fixture
def get_dts_utc_now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


@pytest.fixture
def expected_data_frame(
    spark_session, get_dts_utc_now: datetime.datetime
) -> Generator[DataFrame, None, None]:
    data = [[1, "first_row", get_dts_utc_now], [2, "second_row", get_dts_utc_now]]
    schema = "id INT, label STRING, __aud_timestamp_created TIMESTAMP"

    df = spark_session.createDataFrame(data=data, schema=schema)
    yield df


def test_add_creation_dts(
    dummy_data_frame: DataFrame,
    expected_data_frame: DataFrame,
    get_dts_utc_now: datetime.datetime,
) -> None:
    df = add_creation_dts(df=dummy_data_frame, dts_utc_now=get_dts_utc_now)

    assertDataFrameEqual(df, expected_data_frame)
