---
description: "Learn more about: INFO.STORAGEFILES"
title: "INFO.STORAGEFILES function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGEFILES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each storage file in the semantic model. This function provides metadata about storage files and their characteristics.

## Syntax

```dax
INFO.STORAGEFILES()
```

## Return value

A table whose columns match the schema rowset for storage files in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.STORAGEFILES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.STORAGEFILES(),
        "FileID", [FileID],
        "State", [State],
        "FileSize", [FileSize]
    )
```

## Example 3 - Calculated table

```dax
Storage Files =
SELECTCOLUMNS(
    INFO.STORAGEFILES(),
    "FileID", [FileID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Storage Files =
COUNTROWS(INFO.STORAGEFILES())
```