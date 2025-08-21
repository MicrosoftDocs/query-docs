---
description: "Learn more about: INFO.DICTIONARYSTORAGES"
title: "INFO.DICTIONARYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.DICTIONARYSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each dictionary storage in the semantic model. This function provides metadata about dictionary storage characteristics and compression.

## Syntax

```dax
INFO.DICTIONARYSTORAGES()
```

## Return value

A table whose columns match the schema rowset for dictionary storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.DICTIONARYSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DICTIONARYSTORAGES(),
        "DictionaryID", [DictionaryID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Dictionary Storages =
SELECTCOLUMNS(
    INFO.DICTIONARYSTORAGES(),
    "DictionaryID", [DictionaryID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Dictionary Storages =
COUNTROWS(INFO.DICTIONARYSTORAGES())
```