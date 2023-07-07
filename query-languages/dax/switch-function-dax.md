---
description: "Learn more about: SWITCH"
title: "SWITCH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/06/2023
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# SWITCH

Evaluates an expression against a list of values and returns one of multiple possible result expressions. This function can be used to avoid having multiple nested [IF](if-function-dax.md) statements.  
  
## Syntax  
  
```dax
SWITCH(<expression>, <value>, <result>[, <value>, <result>]…[, <else>])  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| expression  | Any DAX expression that returns a single scalar value where the expression is to be evaluated multiple times (for each row/context).   |  
| value |  A constant value to be matched with the results of *expression*.  |
|result |Any scalar expression to be evaluated if the results of *expression* match the corresponding *value*.  |
|else |Any scalar expression to be evaluated if the result of *expression* doesn't match any of the *value* arguments.  |

## Return value

If there’s a match with a *value*, a scalar value from the corresponding *result* is returned. If there isn’t a match with a *value*, a value from *else* is returned. If none of the *values* match and *else* isn’t specified, BLANK is returned.
  
## Remarks

- The *expression* to be evaluated can be a constant value or an expression. A common use of this function is to set the first parameter to TRUE. See examples below.
- All *result* expressions and the *else* expression must be of the same data type.
- The order of conditions matters. As soon as one *value* matches, the corresponding *result* is returned, and other subsequent *values* aren’t evaluated. Make sure the most restrictive *values* to be evaluated are specified before less restrictive *values*. See examples below.
  
## Examples

A common use of SWITCH is to compare *expression* with constant *values*. The following example creates a calculated column of month names:

```dax
= SWITCH(
         [Month Number Of Year],
         1, "January",
         2, "February",
         3, "March",
         4, "April",
         5, "May",
         6, "June",
         7, "July",
         8, "August",
         9, "September",
         10, "October",
         11, "November",
         12, "December",
         "Unknown month number"
        )
```

Another common use of SWITCH is to replace multiple nested IF statements. This is accomplished by setting expression to TRUE, as shown in the following example, which compares Reorder Point and Safety Stock Level on products to identify potential risks of running out of stock:

```dax
= SWITCH (
        TRUE,
        [Reorder Point] > [Safety Stock Level], "Good: Safety stock level exceeded",
        [Reorder Point] = [Safety Stock Level], "Minimal: Safety stock level met",
        [Reorder Point] < [Safety Stock Level], "At risk: Safety stock level not met",
        ISBLANK ( [Reorder Point] ), "Incomplete: Reorder point not set",
        ISBLANK ( [Safety Stock Level] ), "Incomplete: Safety stock level not set",
        "Unknown"
        )


```

The order of *values* matters. In the following example, the second *result* is never returned because the first value is less restrictive than the second. The result in this example is always “A” or “C”, but never “B”.

```dax
= SWITCH (
         TRUE,
         Product[Standard Cost] < 100, "A",
         Product[Standard Cost] < 10, "B",
         "C"
         )

```

The following statement returns an error because the data types in the *result* arguments are different. Keep in mind that the data types in all *result* and *else* arguments must be the same.

```dax
= SWITCH ([Class],
        "L", "Large",
        "H", 0.1
        )

```
