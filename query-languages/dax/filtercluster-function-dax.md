---
description: "Learn more about: FILTERCLUSTER"
title: "FILTERCLUSTER function (DAX) | Microsoft Docs"
---
# FILTERCLUSTER

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns a correlated join table over a set of groups.  
  
## Syntax  
  
```dax
FILTERCLUSTER( <groupBy_columnName> [, < groupBy_columnName >]…, [<filterTable>]… [, <separator>, <tableScan>…] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|A fully qualified column reference (Table[Column]) to a base table for which the distinct values are included in the returned table. Each groupBy_columnName column is cross-joined (different tables) or auto-existed (same table) with the subsequent specified columns.|  
|filterTable|A table expression participating in the join.|  
|separator|A string literal which serves no purpose other than separating filterTable parameter with tableScan parameter|  
|tableScan|A table scan that joins with filterTable parameters, applying autoexist semantics, and returns columns specified in groupBy_columnName|
  
## Return value

A table which includes combinations of values from the supplied columns based on the grouping specified. The column only includes column specified by groupBy_columnName parameter.
  
## Remarks

- FILTERCLUSTER function can only be used inside GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions.

- FILTERCLUSTER is semantically equivalent to a natural join across all filterTable and tableScan parameters, and then group by columns specified by groupBy_columnName parameters. Group by columns must come from tableScan parameters.

- tableScan parameters are evaluated in the context of filterTable

[SUMMARIZE](summarize-function-dax.md)
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
