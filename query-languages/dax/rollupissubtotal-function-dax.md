---
description: "Learn more about: ROLLUPISSUBTOTAL"
title: "ROLLUPISSUBTOTAL function (DAX) | Microsoft Docs"
---
# ROLLUPISSUBTOTAL

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Pairs rollup groups with the column added by [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md). This function can only be used within an [ADDMISSINGITEMS](addmissingitems-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPISSUBTOTAL ( [<grandTotalFilter>], <groupBy_columnName>, <isSubtotal_columnName> [, [<groupLevelFilter>] [, <groupBy_columnName>, <isSubtotal_columnName> [, [<groupLevelFilter>] [, … ] ] ] ] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|grandTotalFilter|(Optional) Filter to be applied to the grandtotal level.|  
|groupBy_columnName|Name of an existing column used to create summary groups based on the values found in it. Cannot be an expression.|  
|isSubtotal_columnName |Name of an ISSUBTOTAL column. The values of the column are calculated using the ISSUBTOTAL function. |
|groupLevelFilter|(Optional) Filter to be applied to the current level.|

## Return value

None
  
## Remarks  

This function can only be used within an [ADDMISSINGITEMS](addmissingitems-function-dax.md) expression.
