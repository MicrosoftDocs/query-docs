---
description: "Learn more about: ORDERBY"
title: "ORDERBY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 11/29/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# ORDERBY

Defines the columns that determine the sort order within each of a WINDOW function’s partitions.
  
## Syntax  
  
```dax
ORDERBY ( <orderBy_columnName>[, <order>][, orderBy_columnName [, <order>]] [, …] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|orderBy_columnName|The name of an existing column to be used to sort the data within each of a window function’s partitions.|
|order|(Optional) A value that specifies how to sort \<orderBy_columnName> values, ascending or descending:<br> Value: **DESC**. Alternative value: **0**(zero)/**FALSE**. Sorts in descending order of values of \<orderBy_columnName>. <br> Value: **ASC**. Alternative value: **1**/**TRUE**. Sorts in ascending order of values of \<orderBy_columnName>. This is the default value if \<order> is omitted.|

## Return value

This function does not return a value.  
  
## Remarks

This function can only be used within a [WINDOW](window-function-dax.md) function expression.

## Example

See [OFFSET](offset-function-dax.md).

## See also

[INDEX](index-function-dax.md)  
[OFFSET](offset-function-dax.md)  
[PARTITIONBY](partitionby-function-dax.md)  
[WINDOW](window-function-dax.md)