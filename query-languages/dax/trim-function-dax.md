---
description: "Learn more about: TRIM"
title: "TRIM function (DAX)"
---
# TRIM

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Removes all spaces from text except for single spaces between words.

## Syntax

```dax
TRIM(<text>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`text`|The text from which you want spaces removed, or a column that contains text.|

## Return value

The string with spaces removed.

## Remarks

- Use TRIM on text that you have received from another application that may have irregular spacing.

- The TRIM function was originally designed to trim the 7-bit ASCII space character (value 32) from text. In the Unicode character set, there is an additional space character called the nonbreaking space character that has a decimal value of 160. This character is commonly used in Web pages as the HTML entity, &amp;nbsp;. By itself, the TRIM function does not remove this nonbreaking space character. For an example of how to trim both space characters from text, see Remove spaces and nonprinting characters from text.

## Example

The following formula creates a new string that does not have trailing white space.

```dax
= TRIM("A column with trailing spaces.   ")
```

When you create the formula, the formula is propagated through the row just as you typed it, so that you see the original string in each formula and the results are not apparent. However, when the formula is evaluated the string is trimmed.

You can verify that the formula produces the correct result by checking the length of the calculated column created by the previous formula, as follows:

```dax
= LEN([Calculated Column 1])
```

## Related content

[Text functions](text-functions-dax.md)
