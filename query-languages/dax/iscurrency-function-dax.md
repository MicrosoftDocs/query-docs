---
description: "Learn more about: ISCURRENCY"
title: "ISCURRENCY function (DAX)"
ms.custom: ExampleTypeGeneric
---
# ISCURRENCY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a decimal number, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISCURRENCY(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a a decimal number; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This functions is an alias of [ISDECIMAL](/dax/isdecimal-function-dax.md)

## Example

The following DAX query shows the behavior of ISCURRENCY.

```dax
EVALUATE
{
    IF ( ISCURRENCY ( 3.1E-1 ), "Is currency", "Is not currency" ), //RETURNS: Is not currency
    IF ( ISCURRENCY ( "42" ), "Is currency", "Is not currency" ), //RETURNS: Is not currency
    IF ( ISCURRENCY ( 42 ), "Is currency", "Is not currency" ), //RETURNS: Is not currency
    IF ( ISCURRENCY ( CURRENCY ( 4.2421 ) ), "Is currency", "Is not currency" ) //RETURNS: Is currency
}
```

## Related content

- [ISDECIMAL](/dax/isdecimal-function-dax.md)
- [Information functions](information-functions-dax.md)
