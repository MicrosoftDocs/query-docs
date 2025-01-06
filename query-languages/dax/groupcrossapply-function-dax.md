---
description: "Learn more about: GROUPCROSSAPPLY"
title: "GROUPCROSSAPPLY function (DAX) | Microsoft Docs"
---
# GROUPCROSSAPPLY

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns a summary table over a set of groups.  
  
## Syntax  
  
```dax
GROUPCROSSAPPLY( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]…[, <name>, <expression>]…)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table.|  
|filterTable|A table expression which is added to the filter context of all columns specified as groupBy_columnName arguments.|  
|name|A string representing the column name to use for the subsequent expression specified.|  
|expression|Any DAX expression that returns a single value (not a table).|  
  
## Return value

A table which includes combinations of values from the supplied columns based on the grouping specified. Only rows for which at least one of the supplied expressions return a non-blank value are included in the table returned. If all expressions evaluate to BLANK/NULL for a row, that row is not included in the table returned.  
  
## Remarks

- GROUPCROSSAPPLY is similar to SUMMARIZECOLUMNS function, but it does not apply implicit autoexist. All filterTable parameters are cross-join. FILTERCLUSTER function can be used to perform natural joins of filter tables or group by columns if needed.

- You can modify filtering behavior of filterTable by using the following functions:

	- ALLSELECTEDAPPLY

	- ALLSELECTEDREMOVE

	- ALWAYSAPPLY

	- KEEPFILTERS

	- SHADOWCLUSTER

	- NONFILTER

## Related content

[ALLSELECTEDAPPLY function](allselectedapply-function-dax.md)
[ALLSELECTEDREMOVE function](allselectedremove-function-dax.md)
[ALWAYSAPPLY function](alwaysapply-function-dax.md)
[KEEPFILTERS function](keepfilters-function-dax.md)
[SHADOWCLUSTER function](shadowcluster-function-dax.md)
[NONFILTER function](nonfilter-function-dax.md)
[FILTERCLUSTER function](filtercluster-function-dax.md)
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
