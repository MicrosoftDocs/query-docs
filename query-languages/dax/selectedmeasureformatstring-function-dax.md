---
title: "SELECTEDMEASUREFORMATSTRING function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 05/31/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SELECTEDMEASUREFORMATSTRING

Used by expressions for calculation items to retrieve the format string of the measure that is in context.

> [!NOTE]
> This function currently applies only to [SQL Server 2019 Analysis Services CTP 2.3](https://docs.microsoft.com/sql/sql-server/what-s-new-in-sql-server-ver15?view=sqlallproducts-allversions#calc-ctp24) and later.
  
## Syntax  
  
```dax
SELECTEDMEASUREFORMATSTRING()
```
  
### Parameters  
  
None  
  
## Return value  

A string holding the format string of the measure that is currently in context when the calculation item is evaluated.

## Remarks

This function can only be referenced in expressions for calculation items in calculation groups. It is designed to be used by the **Format String Expression** property of calculation items.


## Example  

The following expression is evaluated by the Format String Expression property for a calculation item. If there is a single currency in filter context, the format string is retrieved from the DimCurrency[FormatString] column; otherwise the format string of the measure in context is used.
  
```dax
SELECTEDVALUE( DimCurrency[FormatString], SELECTEDMEASUREFORMATSTRING() )
```
  
## See also  
[SELECTEDMEASURE](selectedmeasure-function-dax.md)  
[ISSELECTEDMEASURE](isselectedmeasure-function-dax.md)   
  
