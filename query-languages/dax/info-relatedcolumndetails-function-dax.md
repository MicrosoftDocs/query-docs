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

|Column|Description|
|---|---|
|ID|Unique identifier for the related column detail|
|ColumnID|Foreign key to the column this detail relates to|
|ModifiedTime|Date and time when the related column detail was last modified|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATEDCOLUMNDETAILS()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _RelatedColumnDetails = 
    SELECTCOLUMNS(
        INFO.RELATEDCOLUMNDETAILS(),
        "ColumnID", [ColumnID],
        "Modified", [ModifiedTime]
    )

VAR _Columns = 
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "ColumnID", [ID],
        "TableID", [TableID],
        "Column Name", [Name],
        "Data Type", [DataType]
    )

VAR _Tables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "TableID", [ID],
        "Table Name", [Name]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _RelatedColumnDetails,
        _Columns
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _Tables
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable2,
        "Table Name", [Table Name],
        "Column Name", [Column Name],
        "Data Type", [Data Type],
        "Modified", [Modified]
    )
ORDER BY [Table Name], [Column Name]
```

## See also

- [INFO.DEPENDENCIES](info-dependencies-function-dax.md)
- [INFO.CALCDEPENDENCY](info-calcdependency-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
