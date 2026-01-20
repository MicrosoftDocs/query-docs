---
description: "Learn more about: ISSTRING"
title: "ISSTRING function (DAX)"
ms.topic: reference
ms.custom: ExampleTypeGeneric
---
# ISSTRING

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks if a value is text, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISSTRING(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to check.|

## Return value

`TRUE` if the value is text; otherwise `FALSE`.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
- This function is an alias of [ISTEXT](istext-function-dax.md).

## Example

The following DAX query shows the behavior of the ISSTRING function.


```dax
EVALUATE
{
    IF ( ISSTRING ( "text" ), "Is Text", "Is Non-Text" ), // RETURNS: Is Text
    IF ( ISSTRING ( "" ), "Is Text", "Is Non-Text" ), // RETURNS: Is Text
    IF ( ISSTRING ( 42 ), "Is Text", "Is Non-Text" ), // RETURNS: Is Non-Text
    IF ( ISSTRING ( BLANK () ), "Is Text", "Is Non-Text" ) // RETURNS: Is Non-Text
}
```

## Related content

- [ISTEXT](istext-function-dax.md)
- [Information functions](information-functions-dax.md)
