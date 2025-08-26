---
description: "Learn more about: INFO.RELATEDCOLUMNDETAILS"
title: "INFO.RELATEDCOLUMNDETAILS function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATEDCOLUMNDETAILS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each related column detail in the semantic model. This function provides metadata about related column details for relationships.

## Syntax

```dax
INFO.RELATEDCOLUMNDETAILS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for related column details in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

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

## See also

[INFO.DEPENDENCIES](info-dependencies-function-dax.md)
[INFO.CALCDEPENDENCY](info-calcdependency-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
