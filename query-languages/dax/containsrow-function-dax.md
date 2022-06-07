---
description: "Learn more about: CONTAINSROW function"
title: "CONTAINSROW function | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/07/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# CONTAINSROW function

Returns TRUE if a row of values exists or contained in a table, otherwise returns FALSE.

## Syntax

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

- Except syntax, the **IN** operator and CONTAINSROW function are functionally equivalent.
  
    ```dax
    <scalarExpr> IN <tableExpr> 
    ( <scalarExpr1>, <scalarExpr2>, … ) IN <tableExpr>
    ```

  - The number of scalarExprN must match the number of columns in tableExpr.
  - NOT IN is not an operator in DAX. To perform the logical negation of the IN operator, put NOT in front of the entire expression. For example, NOT [Color] IN { "Red", "Yellow", "Blue" }.

- Unlike the = operator, the IN operator and the CONTAINSROW function perform strict comparison. For example, the BLANK value does not match 0.

## Examples

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

### Example 1

The following equivalent DAX queries:

```dax
EVALUATE
FILTER (
    ALL ( Product[Color] ),
    [Color]
        IN {
        "Red",
        "Yellow",
        "Blue"
    }
)
ORDER BY [Color]
```

and

```dax
EVALUATE
FILTER (
    ALL ( Product[Color] ),
    ( [Color] )
        IN {
        "Red",
        "Yellow",
        "Blue"
    }
)
ORDER BY [Color]
```

and

```dax
EVALUATE
FILTER (
    ALL ( Product[Color] ),
    CONTAINSROW (
        {
            "Red",
            "Yellow",
            "Blue"
        },
        [Color]
    )
)
ORDER BY [Color]
```

Return the following table with a single column:

[Color]  |
---------|---------
Blue     |
Red     |
Yellow  |

### Example 2

The following equivalent DAX queries:

```dax
EVALUATE
FILTER (
    SUMMARIZE (
        Product,
        [Color],
        [Subcategory]
    ),
    ( [Color], [Subcategory] )
        IN {
        ( "Black", "Road Frames" )
    }
)
```

and

```dax
EVALUATE
FILTER (
    SUMMARIZE (
        Product,
        [Color],
        [Subcategory]
    ),
    ( [Color], [Subcategory] )
        IN {
        ( "Black", "Road Frames" )
    }
)
```

Return the following table:

[Color]  | [Size] |
---------|---------
Black     |  Road Frames

### Example 3

The following equivalent DAX queries:

```dax
EVALUATE
FILTER (
    ALL ( Product[Color] ),
    NOT [Color]
        IN {
        "Red",
        "Yellow",
        "Blue"
    }
)
ORDER BY [Color]
```

and

```dax
EVALUATE
FILTER (
    ALL ( Product[Color] ),
    NOT CONTAINSROW (
        {
            "Red",
            "Yellow",
            "Blue"
        },
        [Color]
    )
)
ORDER BY [Color]
```

Return the following table with a single column:

[Color]  |
---------|---------
Black     |
Grey     |
Multi  |  
NA   |
Silver  |
Silver\Black  |
White |
