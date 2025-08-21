---
description: "Learn more about: INFO.ATTRIBUTEHIERARCHYSTORAGES"
title: "INFO.ATTRIBUTEHIERARCHYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.ATTRIBUTEHIERARCHYSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each attribute hierarchy storage in the semantic model. This function provides metadata about the storage characteristics of attribute hierarchies.

## Syntax

```dax
INFO.ATTRIBUTEHIERARCHYSTORAGES()
```

## Return value

A table whose columns match the schema rowset for attribute hierarchy storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.ATTRIBUTEHIERARCHYSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.ATTRIBUTEHIERARCHYSTORAGES(),
        "AttributeHierarchyID", [AttributeHierarchyID],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Attribute Hierarchy Storages =
SELECTCOLUMNS(
    INFO.ATTRIBUTEHIERARCHYSTORAGES(),
    "AttributeHierarchyID", [AttributeHierarchyID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Attribute Hierarchy Storages =
COUNTROWS(INFO.ATTRIBUTEHIERARCHYSTORAGES())
```