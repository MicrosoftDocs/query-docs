---
title: "LASTNONBLANK function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# LASTNONBLANK

Returns the last value in the column, **column**, filtered by the current context, where the expression is not blank.  
  
## Syntax  
  
```dax
LASTNONBLANK(<column>,<expression>)  
```
  
### Parameters  
  
|||  
|-|-|  
|Term|Definition|  
|column|A column expression.|  
|expression|An expression evaluated for blanks for each value of **column**.|  
  
## Return value

A table containing a single column and single row with the computed last value.  
  
## Remarks

- The **column** argument can be any of the following:  
  - A reference to any column.  
  - A table with a single column.  
  - A Boolean expression that defines a single-column table  
  
- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).  
  
- This function is typically used to return the last value of a column for which the expression is not blank. For example, you could get the last value for which there were sales of a product.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## See also

[FIRSTNONBLANK function](firstnonblank-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
[DAX function reference](dax-function-reference.md)  
