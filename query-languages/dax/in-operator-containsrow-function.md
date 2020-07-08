---
title: "IN Operator / CONTAINSROW function | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# IN Operator / CONTAINSROW function

Returns TRUE if a row of values exists or contained in a table, otherwise returns FALSE.
Except syntax, the IN operator and CONTAINSROW function are functionally equivalent.

## IN Operator

### Syntax
  
```dax
<scalarExpr> IN <tableExpr> 
( <scalarExpr1>, <scalarExpr2>, … ) IN <tableExpr>

```

## CONTAINSROW function

### Syntax

```dax
CONTAINSROW(<tableExpr>, <scalarExpr>[, <scalarExpr>, …]) 
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|scalarExprN|Any valid DAX expression that returns a scalar value.|  
|tableExpr|Any valid DAX expression that returns a table of data.|  

## Return value

TRUE or FALSE.
  
## Remarks

- The number of scalarExprN must match the number of columns in tableExpr.

- Unlike the = operator, the IN operator and the CONTAINSROW function perform strict comparison. For example, the BLANK value does not match 0.

- NOT IN is not an operator in DAX. To perform the logical negation of the IN operator, put NOT in front of the entire expression. For example, NOT [Color] IN { "Red", "Yellow", "Blue" }.

## Example 1

The following equivalent DAX queries:

```dax
EVALUATE FILTER(ALL(DimProduct[Color]), [Color] IN { "Red", "Yellow", "Blue" })
ORDER BY [Color]
```

and

```dax
EVALUATE FILTER(ALL(DimProduct[Color]), ([Color]) IN { "Red", "Yellow", "Blue" })
ORDER BY [Color]
```

and

```dax
EVALUATE FILTER(ALL(DimProduct[Color]), CONTAINSROW({ "Red", "Yellow", "Blue" }, [Color]))
ORDER BY [Color]
```

Return the following table with a single column:

DimProduct[Color]  | |
---------|---------
Blue     |
Red     |
Yellow  |

## Example 2

The following equivalent DAX queries:

```dax
EVALUATE FILTER(SUMMARIZE(DimProduct, [Color], [Size]), ([Color], [Size]) IN { ("Black", "L") }) 
```

and

```dax
EVALUATE FILTER(SUMMARIZE(DimProduct, [Color], [Size]), CONTAINSROW({ ("Black", "L") }, [Color], [Size]))
```

Return:

DimProduct[Color]  | DimProduct[Size] |
---------|---------
Black     |  L

### Example 3

The following equivalent DAX queries:

```dax
EVALUATE FILTER(ALL(DimProduct[Color]), NOT [Color] IN { "Red", "Yellow", "Blue" })
ORDER BY [Color]
```

and

```dax
EVALUATE FILTER(ALL(DimProduct[Color]), NOT CONTAINSROW({ "Red", "Yellow", "Blue" }, [Color]))
ORDER BY [Color]
```

Return the following table with a single column:

DimProduct[Color]  | |
---------|---------
Black     |
Grey     |
Multi  |  
NA   |
Silver  |
Silver\Black  |
White |
