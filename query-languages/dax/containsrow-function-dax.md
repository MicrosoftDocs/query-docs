---
description: "Learn more about: CONTAINSROW function"
title: "CONTAINSROW function | Microsoft Docs"
---
# CONTAINSROW function

Returns TRUE if there exists at least one row where all columns have specified values.

## Syntax

```dax
CONTAINSROW(<Table>, <Value> [, <Value> [, …] ] ) 
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Table|A table to test.|  
|Value|Any valid DAX expression that returns a scalar value.|  

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

The following DAX queries:

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

## Related content

[IN operator](dax-operator-reference.md#logical-operators)  
[DAX queries](dax-queries.md)
