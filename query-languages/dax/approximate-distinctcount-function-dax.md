---
description: "Learn more about: APPROXIMATEDISTINCTCOUNT"
title: "APPROXIMATEDISTINCTCOUNT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# APPROXIMATEDISTINCTCOUNT

Returns the *approximate* number of rows that contain distinct values in a column. This function can query large amounts of data with potentially better performance than DISTINCTCOUNT, with slight deviation from the exact result.
  
## Syntax  
  
```dax
APPROXIMATEDISTINCTCOUNT(<columnName>)
```
  
### Parameters  

|Term  |Description|  
|---------|---------|
|column     | The column that contains the values to be counted. This cannot be an expression.  |

## Return value

The approximate number of distinct values in *column*.  
  
## Remarks  

The only argument to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.
