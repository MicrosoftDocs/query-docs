---
description: "Learn more about: MAX"
title: "MAX function (DAX) | Microsoft Docs"
---
# MAX

Returns the largest value in a column, or between two scalar expressions.  
  
## Syntax  
  
```dax
MAX(<column>)  
```

```dax
MAX(<expression1>, <expression2>)
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|column|The column in which you want to find the largest value.|  
|expression|Any DAX expression which returns a single value.|  
  
## Return value

The largest value.
  
## Remarks  

- When comparing two expressions, blank is treated as 0 when comparing. That is, Max(1, Blank() ) returns 1, and Max( -1, Blank() ) returns 0. If both arguments are blank, MAX returns a blank. If either expression returns a value which is not allowed, MAX returns an error.

- TRUE/FALSE values are not supported. If you want to evaluate a column of TRUE/FALSE values, use the MAXA function.
  
## Example 1

The following example returns the largest value found in the ExtendedAmount column of the InternetSales table.  
  
```dax
= MAX(InternetSales[ExtendedAmount])  
```

## Example 2

The following example returns the largest value between the result of two expressions.  
  
```dax
= Max([TotalSales], [TotalPurchases])
```

## See also

[MAXA function](maxa-function-dax.md)  
[MAXX function](maxx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
