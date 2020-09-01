---
title: "ROLLUPISSUBTOTAL function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ROLLUPISSUBTOTAL

Pairs rollup groups with the column added by [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md). This function can only be used within an [ADDMISSINGITEMS](addmissingitems-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPISSUBTOTAL ( [<GrandtotalFilter>], <GroupBy_ColumnName>, <IsSubtotal_ColumnName> [, [<GroupLevelFilter>] [, <GroupBy_ColumnName>, <IsSubtotal_ColumnName> [, [<GroupLevelFilter>] [, … ] ] ] ] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|GrandtotalFilter|(Optional) Filter to be applied to the grandtotal level.|  
|GroupBy_ColumnName|Name of an existing column to be used to create summary groups based on the values found in it. Cannot be an expression.|  
|IsSubtotal_ColumnName |Name of an ISSUBTOTAL column.|
|GroupLevelFilter|(Optional) Filter to be applied to the current level.|

## Return value

None
  
## Remarks  

This function can only be used within an [ADDMISSINGITEMS](addmissingitems-function-dax.md) expression.

## Example

See [ADDMISSINGITEMS](addmissingitems-function-dax.md).
