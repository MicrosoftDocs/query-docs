---
description: "Learn more about: ROLLUPADDISSUBTOTAL"
title: "ROLLUPADDISSUBTOTAL function (DAX)"
---
# ROLLUPADDISSUBTOTAL

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Modifies the behavior of the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function by adding rollup/subtotal rows to the result based on the groupBy_columnName columns. This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPADDISSUBTOTAL ( [<grandtotalFilter>], <groupBy_columnName>, <name> [, [<groupLevelFilter>] [, <groupBy_columnName>, <name> [, [<groupLevelFilter>] [, … ] ] ] ] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|`grandtotalFilter`|(Optional) Filter to be applied to the grandtotal level.|  
|`groupBy_columnName`|Name of an existing column used to create summary groups based on the values found in it. Cannot be an expression.|  
|name |Name of an ISSUBTOTAL column. The values of the column are calculated using the ISSUBTOTAL function.|
|`groupLevelFilter`|(Optional) Filter to be applied to the current level.|

## Return value

The function does not return a value.
  
## Remarks  

None

## Example

See [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
