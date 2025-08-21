---
description: "Learn more about: INFO.RELATEDCOLUMNDETAILS"
title: "INFO.RELATEDCOLUMNDETAILS function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATEDCOLUMNDETAILS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each related column detail in the semantic model. This function provides metadata about related column details for relationships.

## Syntax

```dax
INFO.RELATEDCOLUMNDETAILS()
```

## Return value

A table whose columns match the schema rowset for related column details in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.RELATEDCOLUMNDETAILS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.RELATEDCOLUMNDETAILS(),
        "Name", [Name],
        "ExplicitName", [ExplicitName],
        "RelationshipID", [RelationshipID]
    )
```

## Example 3 - Calculated table

```dax
Related Column Details =
SELECTCOLUMNS(
    INFO.RELATEDCOLUMNDETAILS(),
    "Name", [Name],
    "ExplicitName", [ExplicitName]
)
```

## Example 4 - Measure

```dax
Number of Related Column Details =
COUNTROWS(INFO.RELATEDCOLUMNDETAILS())
```