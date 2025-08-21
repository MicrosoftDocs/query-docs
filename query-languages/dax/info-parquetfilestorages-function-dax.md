---
description: "Learn more about: INFO.PARQUETFILESTORAGES"
title: "INFO.PARQUETFILESTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.PARQUETFILESTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each Parquet file storage in the semantic model. This function provides metadata about Parquet file storage characteristics.

## Syntax

```dax
INFO.PARQUETFILESTORAGES()
```

## Return value

A table whose columns match the schema rowset for Parquet file storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PARQUETFILESTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PARQUETFILESTORAGES(),
        "FileID", [FileID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Parquet File Storages =
SELECTCOLUMNS(
    INFO.PARQUETFILESTORAGES(),
    "FileID", [FileID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Parquet File Storages =
COUNTROWS(INFO.PARQUETFILESTORAGES())
```