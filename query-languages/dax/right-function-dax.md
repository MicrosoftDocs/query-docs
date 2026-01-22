---
description: "Learn more about: RIGHT"
title: "RIGHT function (DAX)"
ms.topic: reference
---
# RIGHT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

RIGHT returns the last character or characters in a text string, based on the number of characters you specify.

## Syntax

```dax
RIGHT(<text>, <num_chars>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|The text string that contains the characters you want to extract, or a reference to a column that contains text.|
|`num_chars`|(optional) The number of characters you want RIGHT to extract; is omitted, 1. You can also use a reference to a column that contains numbers.|

If the column reference does not contain text, it is implicitly cast as text.

## Return value

A text string containing the specified right-most characters.

## Remarks

- [!INCLUDE [function-unicodecharacterbehavior](includes/function-unicodecharacterbehavior.md)]

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example: Returning a Fixed Number of Characters

The following formula returns the last two digits of the product code in the New Products table.

```dax
= RIGHT('New Products'[ProductCode],2)
```

## Example: Using a Column Reference to Specify Character Count

The following formula returns a variable number of digits from the product code in the New Products table, depending on the number in the column, MyCount. If there is no value in the column, MyCount, or the value is a blank, RIGHT also returns a blank.

```dax
= RIGHT('New Products'[ProductCode],[MyCount])
```

## Related content

- [Text functions](text-functions-dax.md)
- [LEFT](left-function-dax.md)
- [MID](mid-function-dax.md)

