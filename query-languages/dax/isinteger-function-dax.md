---
description: "Learn more about: ISINTEGER"
title: "ISINTEGER function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISINTEGER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a whole number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISINTEGER(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a whole number; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISINT64](isint64-function-dax.md).

## Example

The following DAX query shows the behavior of ISINTEGER.

```dax
EVALUATE
{
    IF ( ISINTEGER ( 4.2 ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINTEGER ( 3.1E-1 ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINTEGER ( "42" ), "Is integer", "Is not integer" ), // RETURNS: Is not integer
    IF ( ISINTEGER ( 42 ), "Is integer", "Is not integer" ) // RETURNS: Is integer
}
```

## Related content

- [ISINTEGER](isinteger-function-dax.md)
- [Information functions](information-functions-dax.md)
