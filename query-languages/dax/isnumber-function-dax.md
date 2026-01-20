---
description: "Learn more about: ISNUMBER"
title: "ISNUMBER function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISNUMBER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISNUMBER(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is numeric; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISNUMERIC](isnumeric-function-dax.md).

## Example

The following DAX query shows the behavior of ISNUMBER.

```dax
EVALUATE
{
    IF ( ISNUMBER ( 0 ), "Is number", "Is Not number" ), // RETURNS: Is number
    IF ( ISNUMBER ( 3.1E-1 ), "Is number", "Is Not number" ), // RETURNS: Is number
    IF ( ISNUMBER ( "42" ), "Is number", "Is Not number" ) // RETURNS: Is Not number
}
```

## Related content

- [ISNUMERIC](isnumeric-function-dax.md)
- [Information functions](information-functions-dax.md)
