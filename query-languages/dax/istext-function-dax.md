---
description: "Learn more about: ISTEXT"
title: "ISTEXT function (DAX)"
ms.custom: ExampleTypeGeneric
---
# ISTEXT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks if a value is text, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISTEXT(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to check.|

## Return value

`TRUE` if the value is text; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISSTRING](isstring-function-dax.md).

## Example

The following DAX query shows the behavior of the ISTEXT function.

```dax
EVALUATE
{
    IF ( ISTEXT ( "text" ), "Is Text", "Is Non-Text" ), // RETURNS: Is Text
    IF ( ISTEXT ( "" ), "Is Text", "Is Non-Text" ), // RETURNS: Is Text
    IF ( ISTEXT ( 42 ), "Is Text", "Is Non-Text" ), // RETURNS: Is Non-Text
    IF ( ISTEXT ( BLANK () ), "Is Text", "Is Non-Text" ) // RETURNS: Is Non-Text
}
```

## Related content

- [ISSTRING](isstring-function-dax.md)
- [Information functions](information-functions-dax.md)
