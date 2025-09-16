---
description: "Learn more about: ISDATETIME"
title: "ISDATETIME function (DAX)"
ms.custom: ExampleTypeGeneric
---
# ISDATETIME

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is a date / time, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISDATETIME(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

`TRUE` if the value is a date / time; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query shows the behavior of ISDATETIME.

```dax
EVALUATE
{
    IF ( ISDATETIME ( 42 ), "Is datetime", "Is not datetime" ), // RETURNS: Is not datetime
    IF ( ISDATETIME ( "42" ), "Is datetime", "Is not datetime" ), // RETURNS: Is not datetime
    IF ( ISDATETIME ( "2025-07-01" ), "Is datetime", "Is not datetime" ), // RETURNS: Is not datetime
    IF ( ISDATETIME ( dt"2025-07-01" ), "Is datetime", "Is not datetime" ), // RETURNS: Is datetime
    IF ( ISDATETIME ( DATE ( 2025, 7, 1 ) ), "Is datetime", "Is not datetime" ) // RETURNS: Is datetime
}
```

## Related content

- [Information functions](information-functions-dax.md)
