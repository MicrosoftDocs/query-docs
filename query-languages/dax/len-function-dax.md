---
description: "Learn more about: LEN"
title: "LEN function (DAX)"
ms.topic: reference
---
# LEN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the number of characters in a text string.

## Syntax

```dax
LEN(<text>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|The text whose length you want to find, or a column that contains text. Spaces count as characters.|

## Return value

A whole number indicating the number of characters in the text string.

## Remarks

- Whereas Microsoft Excel has different functions for working with single-byte and double-byte character languages, DAX uses Unicode and stores all characters with the same length.

- If you use LEN with a column that contains non-text values, such as dates or Booleans, the function implicitly casts the value to text, using the current column format.

- [!INCLUDE [function-unicodecharacterbehavior](includes/function-unicodecharacterbehavior.md)]

## Example

The following formula sums the lengths of addresses in the columns, [AddressLine1] and [AddressLine2].

```dax
= LEN([AddressLine1])+LEN([AddressLin2])
```
