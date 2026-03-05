---
description: "Learn more about: GROUPCROSSAPPLYTABLE"
title: "GROUPCROSSAPPLYTABLE function (DAX) | Microsoft Docs"
ms.topic: reference
---
# GROUPCROSSAPPLYTABLE

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns a summary table over a set of groups.  
  
## Syntax  
  
```dax
GROUPCROSSAPPLYTABLE( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]… [, <separator>, <table expression>] )  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table.|  
|filterTable|A table expression which is added to the filter context of all columns specified as groupBy_columnName arguments. The values present in the filter table are used to filter before cross-join/auto-exist is performed.|  
|separator|A string literal which serves no purpose other than separating filterTable parameter with table expression parameter|  
|table expression|A table expression that is evaluated under filter context of filterTable parameters and returned as a part of the join in the return value|
  
## Return value

A table which includes combinations of values from the supplied columns based on the grouping specified.
  
## Remarks

- GROUPCROSSAPPLYTABLE is similar to GROUPCROSSJOIN function. All filterTable parameters are cross-join. FILTERCLUSTER function can be used to perform natural joins of filter tables or group by columns if needed.

- The table expression parameter is evaluated in the filter context containing all filterTable parameters.

- You can modify filtering behavior of filterTable by using the following functions:

	- ALLSELECTEDAPPLY

	- ALLSELECTEDREMOVE

	- ALWAYSAPPLY

	- KEEPFILTERS

	- SHADOWCLUSTER

	- NONFILTER

## Related content

- [ALLSELECTEDAPPLY function](allselectedapply-function-dax.md)
- [ALLSELECTEDREMOVE function](allselectedremove-function-dax.md)
- [ALWAYSAPPLY function](alwaysapply-function-dax.md)
- [KEEPFILTERS function](keepfilters-function-dax.md)
- [SHADOWCLUSTER function](shadowcluster-function-dax.md)
- [NONFILTER function](nonfilter-function-dax.md)
- [FILTERCLUSTER function](filtercluster-function-dax.md)
- [GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
