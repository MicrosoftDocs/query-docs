---
description: "Learn more about: ISTEXT"
title: "ISTEXT function (DAX)"
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

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following examples show the behavior of the ISTEXT function.

```dax
//RETURNS: Is Text
= IF(ISTEXT("text"), "Is Text", "Is Non-Text")

//RETURNS: Is Text
= IF(ISTEXT(""), "Is Text", "Is Non-Text")

//RETURNS: Is Non-Text
= IF(ISTEXT(1), "Is Text", "Is Non-Text")

//RETURNS: Is Non-Text
= IF(ISTEXT(BLANK()), "Is Text", "Is Non-Text")
```

## Related content

[Information functions](information-functions-dax.md)
