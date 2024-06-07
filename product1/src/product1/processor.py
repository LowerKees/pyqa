"""Processes incoming data frame into data products as described by ..."""

import datetime

from pyspark.sql import DataFrame
from pyspark.sql.functions import lit


def add_creation_dts(df: DataFrame, dts_utc_now: datetime.datetime) -> DataFrame:
    """Adds a metadata column to a data frame.

    Args:
        df: data frame to add the auditing column to
        dts_utc_now: datetime.datetime object containing current timestamp
            in UTC timezone.

    Returns:
        data frame containing the new column.
    """
    df = df.withColumn("__aud_timestamp_created", lit(dts_utc_now))
    return df
