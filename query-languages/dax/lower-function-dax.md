---
description: "Learn more about: LOWER"
title: "LOWER function (DAX)"
---
# LOWER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts all letters in a text string to lowercase.

## Syntax

```dax
LOWER(<text>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|The text you want to convert to lowercase, or a reference to a column that contains text.|

## Return value

Text in lowercase.

## Remarks

Characters that are not letters are not changed. For example, the formula `= LOWER("123ABC")` returns `123abc`.

## Example

The following formula gets each row in the column, [ProductCode], and converts the value to all lowercase. Numbers in the column are not affected.

```dax
= LOWER('New Products'[ProductCode])
```

## Related content

[Text functions](text-functions-dax.md)
