---
description: "Learn more about: SUM"
title: "SUM function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SUM

Adds all the numbers in a column.  
  
## Syntax  
  
```dax
SUM(<column>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers to sum.|  
  
## Return value

A decimal number.  
  
## Remarks  
  
If you want to filter the values that you are summing, you can use the SUMX function and specify an expression to sum over.  
  
## Example

The following example adds all the numbers that are contained in the column, Amt, from the table, Sales.  
  
```dax
= SUM(Sales[Amt])  
```
  
## See also

[SUMX](sumx-function-dax.md)
