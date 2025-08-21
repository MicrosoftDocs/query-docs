---
description: "Learn more about: INFO.CSDLMETADATA"
title: "INFO.CSDLMETADATA function (DAX)"
author: jeroenterheerdt
---
# INFO.CSDLMETADATA

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about the CSDL metadata in the semantic model. This function provides metadata about the Conceptual Schema Definition Language representation of the model.

## Syntax

```dax
INFO.CSDLMETADATA()
```

## Return value

A table whose columns match the schema rowset for CSDL metadata in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.CSDLMETADATA()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CSDLMETADATA(),
        "Metadata", [METADATA],
        "Version", [VERSION]
    )
```

## Example 3 - Calculated table

```dax
CSDL Metadata =
SELECTCOLUMNS(
    INFO.CSDLMETADATA(),
    "Metadata", [METADATA],
    "Version", [VERSION]
)
```

## Example 4 - Measure

```dax
Number of CSDL Metadata Entries =
COUNTROWS(INFO.CSDLMETADATA())
```