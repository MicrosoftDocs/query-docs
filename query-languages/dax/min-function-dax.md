---
title: "MIN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/19/2019
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MIN

Returns the smallest value in a column, or between two scalar expressions.
  
## Syntax  
  
```dax
MIN(<column>)  
```

```dax
MIN(<expression1>, <expression2>)
```

#### Parameters
  
|Term|Definition|  
|--------|--------------|  
|column|The column in which you want to find the smallest value.|  
|expression|Any DAX expression which returns a single value.|  
  
## Return value

The smallest value.  
  
## Remarks

The MIN function takes a column or two expressions as an argument, and returns the smallest value. The following types of values in the columns are counted:  
  
- Numbers

- Texts

- Dates  

- Blanks

When comparing expressions, blank is treated as 0 when comparing. That is, Min(1,Blank() ) returns 0, and Min( -1, Blank() ) returns -1. If both arguments are blank, MIN returns a blank. If either expression returns a value which is not allowed, MIN returns an error.

TRUE/FALSE values are not supported. If you want to evaluate a column of TRUE/FALSE values, use the MINA function.
  
## Example 1

The following example returns the smallest value from the calculated column, ResellerMargin.  
  
```dax
=MIN([ResellerMargin])  
```
  
## Example 2

The following example returns the smallest value from a column that contains dates and times, TransactionDate. This formula therefore returns the date that is earliest.  
  
```dax
=MIN([TransactionDate])  
```

## Example 3

The following example returns the smallest value from the result of two scalar expressions.  
  
```dax
=Min([TotalSales], [TotalPurchases]) 
```

  
## See also

[MINA function &#40;DAX&#41;](mina-function-dax.md)  
[MINX function &#40;DAX&#41;](minx-function-dax.md)  
[Statistical functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
