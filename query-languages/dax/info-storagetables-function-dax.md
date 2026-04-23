---
description: "Learn more about: INFO.STORAGETABLES"
title: "INFO.STORAGETABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGETABLES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about all table storage in the semantic model. This information helps you understand the model.

## Syntax

```dax
INFO.STORAGETABLES([<Restriction name>, <Restriction value>], ...)
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| [Database_Name]|The name of the database|
| [Cube_Name]|The name of the cube|
| [Measure_Group_Name]|The name of the measure group|
| [Dimension_Name]|The name of the dimension|
| [Table_ID]|The ID of the table|
| [Table_Partitions_Count]|The table partition count|
| [Hint_Table_Type]|The hint of the table type|
| [Rows_Count]|The row count|
| [RIViolation_Count]|This is a deprecated column set to 0.|


## Remarks

Can only be run by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in [DAX queries](/dax/dax-queries), and can't be used in calculations.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGETABLES()
```
## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
