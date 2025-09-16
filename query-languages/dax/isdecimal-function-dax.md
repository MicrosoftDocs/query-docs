---
description: "Learn more about: ISDECIMAL"
title: "ISDECIMAL function (DAX)"
ms.custom: ExampleTypeGeneric
---
# ISDECIMAL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a decimal number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISDECIMAL(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a decimal number; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This functions is an alias of [ISCURRENCY](iscurrency-function-dax.md).

## Example

The following DAX query shows the behavior of ISDECIMAL.

```dax
EVALUATE
{
    IF ( ISDECIMAL ( 3.1E-1 ), "Is decimal", "Is not decimal" ), // RETURNS: Is not decimal
    IF ( ISDECIMAL ( "42" ), "Is decimal", "Is not decimal" ), // RETURNS: Is not decimal
    IF ( ISDECIMAL ( 42 ), "Is decimal", "Is not decimal" ), // RETURNS: Is not decimal
    IF ( ISDECIMAL ( CURRENCY ( 4.2421 ) ), "Is decimal", "Is not decimal" ) // RETURNS: Is decimal
}
```

## Related content

- [ISCURRENCY](iscurrency-function-dax.md)
- [Information functions](information-functions-dax.md)
