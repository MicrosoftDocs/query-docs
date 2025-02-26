---
description: "Learn more about: UPPER"
title: "UPPER function (DAX)"
---
# UPPER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts a text string to all uppercase letters.

## Syntax

```dax
UPPER (<text>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|The text you want converted to uppercase, or a reference to a column that contains text.|

## Return value

Same text, in uppercase.

## Example

The following formula converts the string in the column, [ProductCode], to all uppercase. Non-alphabetic characters are not affected.

```dax
= UPPER(['New Products'[Product Code])
```

## Related content

[Text functions](text-functions-dax.md)
[LOWER function](lower-function-dax.md)
