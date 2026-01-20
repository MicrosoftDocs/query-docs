---
description: "Learn more about: ISDOUBLE"
title: "ISDOUBLE function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISDOUBLE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a floating-point number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISDOUBLE(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a floating-point number; otherwise `FALSE`.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query shows the behavior of ISDOUBLE.

```dax
EVALUATE
{
    IF ( ISDOUBLE ( 4.2 ), "Is double", "Is not double" ), // RETURNS: Is double
    IF ( ISDOUBLE ( 3.1E-1 ), "Is double", "Is not double" ), // RETURNS: Is double
    IF ( ISDOUBLE ( "42" ), "Is double", "Is not double" ), // RETURNS: Is not double
    IF ( ISDOUBLE ( 42 ), "Is double", "Is not double" ), // RETURNS: Is not double
}
```

## Related content

[Information functions](information-functions-dax.md)
