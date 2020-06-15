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
> This function is not compatible with SQL Server 2017 Analysis Services and earlier.
  
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
  
