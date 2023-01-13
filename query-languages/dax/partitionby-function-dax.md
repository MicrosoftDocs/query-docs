---
description: "Learn more about: PARTITIONBY"
title: "PARTITIONBY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 11/29/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# PARTITIONBY

Defines the columns that are used to partition a window function’s \<relation> parameter.
  
## Syntax  
  
```dax
PARTITIONBY ( <partitionBy_columnName>[, partitionBy_columnName [, …] ] )
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|partitionBy_columnName|The name of an existing column to be used to partition the window function’s \<relation>. |

## Return value

This function does not return a value.  
  
## Remarks

This function can only be used within a window function expression.

## Example

See [OFFSET](offset-function-dax.md).

## See also

[INDEX](index-function-dax.md)  
[OFFSET](offset-function-dax.md)  
[ORDERBY](orderby-function-dax.md)  
[WINDOW](window-function-dax.md)  
[RANK](rank-function-dax.md)  
[ROWNUMBER](rownumber-function-dax.md)