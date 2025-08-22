---
description: "Learn more about: INFO.DELTATABLEMETADATASTORAGES"
title: "INFO.DELTATABLEMETADATASTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.DELTATABLEMETADATASTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each delta table metadata storage in the semantic model. This function provides metadata about delta table storage characteristics.

## Syntax

```dax
INFO.DELTATABLEMETADATASTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for delta table metadata storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DELTATABLEMETADATASTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DELTATABLEMETADATASTORAGES(),
        "TableID", [TableID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Delta Table Metadata Storages =
SELECTCOLUMNS(
    INFO.DELTATABLEMETADATASTORAGES(),
    "TableID", [TableID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Delta Table Metadata Storages =
COUNTROWS(INFO.DELTATABLEMETADATASTORAGES())
```