---
description: "Learn more about: ISINT64"
title: "ISINT64 function (DAX)"
ms.custom: ExampleTypeGeneric
---
# ISINT64

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a whole number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISINT64(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a whole number; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISINTEGER](isinteger-function-dax.md).

## Example

The following DAX query shows the behavior of ISINT64.

```dax
EVALUATE
{
    IF ( ISINT64 ( 4.2 ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINT64 ( 3.1E-1 ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINT64 ( "42" ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINT64 ( 42 ), "Is integer", "Is not integer" ) // RETURNS: Is integer
}
```

## Related content

- [ISINTEGER](isinteger-function-dax.md)
- [Information functions](information-functions-dax.md)
