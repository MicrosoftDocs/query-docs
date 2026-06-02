---
description: "Learn more about: FUNCTION"
title: "FUNCTION keyword (DAX)"
ms.topic: reference
---
# FUNCTION

Introduces a function definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      FUNCTION <function name> = ([<parameter name> [: [<type>] [<subtype>] [<passing mode>]] [= <default expression>], ...]) => <function body>
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

|Term|Definition|
|---------|---------|
|`function name`| The name of a function.|
|`parameter name`| The name of the parameter. This cannot be a reserved keyword such as `measure`.|
|`type`| The parameter type. Can be one of the following: `ANYVAL`, `SCALAR`, `TABLE`, `ANYREF`, `CALENDARREF`, `COLUMNREF`, `MEASUREREF`, `TABLEREF`. `ANYVAL` is an abstract type for `SCALAR` or `TABLE`. `ANYREF` is an abstract type for all references.|
|`subtype`| The parameter subtype. Applies only to `parameter type` = `SCALAR`. Can be one of the following: `BOOLEAN`, `DATETIME`, `DECIMAL`, `DOUBLE`, `INT64`, `NUMERIC`, `STRING`, `VARIANT`.|
|`passing mode`| The parameter passing mode. Can be `VAL` (eagerly evaluated) or `EXPR` (lazily evaluated).|
|`default expression`| A DAX expression used when the argument is omitted by the caller. Makes the parameter optional.|
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
