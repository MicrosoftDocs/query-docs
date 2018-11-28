---
title: "SUM function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 9/25/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SUM function (DAX)
Adds all the numbers in a column.  
  
## Syntax  
  
```dax
SUM(<column>)  
```
  
#### Parameters  
  
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
=SUM(Sales[Amt])  
```
  
## See also  
[SUMX function &#40;DAX&#41;](sumx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
