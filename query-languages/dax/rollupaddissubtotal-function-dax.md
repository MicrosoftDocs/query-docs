---
title: "ROLLUPADDISSUBTOTAL function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ROLLUPADDISSUBTOTAL

Modifies the behavior of the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function by adding roll-up/subtotal rows to the result based on the groupBy_columnName columns. This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPADDISSUBTOTAL ( [<filter> …, ] <groupBy_columnName>, <isSubtotal_columnName>[, <filter> …][, <groupBy_columnName >, <isSubtotal_columnName>[, <filter> …]…] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|groupBy_columnName|The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.|  
|isSubtotal_columnName|The name of the Boolean column to be added to the result indicating whether or not a row is a subtotal over the groupBy column, or columns when used with ROLLUPGROUP. This value is calculated using the ISSUBTOTAL function.|  
|filter    | A table expression which is added to the filter context at the current grouping level. A filter before the first group-by column is applied at the grand total level.

## Return value

The function does not return a value.
  
## Remarks  

None

## Example

See [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
