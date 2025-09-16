---
description: "Learn more about: FUNCTION"
title: "FUNCTION keyword (DAX)"
---
# FUNCTION

Introduces a function definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      FUNCTION <function name> = ([parameter name] : [parameter type] [parameter subtype] [parameter passing mode], ...) => <function body>
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

|Term|Definition|
|---------|---------|
|`function name`|The name of a function.|
|`parameter name`|The name of the parameter. This cannot be a reserved keyword such as `measure`.|
|`parameter type`|`anyval`, `scalar`, `table` or `anyref`. `Anyval` is an abstract type for `scalar` or `table`. `Anyref` is an abstract type for all references.| 
|`parameter subtype`|applies only to `parameter type` = `scalar`. Can be one of the following: `boolean`, `datetime`, `decimal`, `double`, `int64`, `numeric`, `string`, `variant`.|
|`parameter passing mode`|`val` (eargerly evaluated) or `expr` (lazily evaluated).|
|`function body`| A DAX expression for the function.  |

## Return value

The calculated result of the function body.

## Remarks

- To learn more about DAX User Defined Functions, see [DAX User Defined Functions](best-practices/dax-user-defined-functions.md).
- To learn more about how FUNCTION statements are used, see [DAX queries](dax-queries.md).

## Related content

- [Working with DAX User Defined Functions](best-practices/dax-user-defined-functions.md)
- [DEFINE](define-statement-dax.md)
- [EVALUATE](evaluate-statement-dax.md)
- [DAX queries](dax-queries.md)
