---
title: "Custom numeric formats for the FORMAT function | Microsoft Docs"
ms.service: powerbi 
ms.date: 11/30/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Custom numeric formats for the FORMAT function

This article describes custom, user-defined formats for numeric values in a FORMAT expression.

## Different formats for different numeric values

A user-defined format expression for numbers can have from one to three sections separated by semicolons. If the format argument contains one of the named numeric formats, only one section is allowed.

|If you use|The result is|
|:-----|:-----|
|One section only|The format expression applies to all values.|
|Two sections|The first section applies to positive values and zeros, the second to negative values.|
|Three sections|The first section applies to positive values, the second to negative values, and the third to zeros.|

```dax
"$#,##0;($#,##0)"
```

If you include semicolons with nothing between them, the missing section is defined using the format of the positive value. For example, the following format displays positive and negative values using the format in the first section and displays "Zero" if the value is zero.

```dax
"$#,##0
```

## User-defined numeric formats

The following table identifies characters you can use to create user-defined number formats.

|Character|Description|
|:-----|:-----|
|None|Display the number with no formatting.|
|(**0**)|Digit placeholder. Display a digit or a zero. If the expression has a digit in the position where the 0 appears in the format string, display it; otherwise, display a zero in that position.If the number has fewer digits than there are zeros (on either side of the decimal) in the format expression, display leading or trailing zeros. If the number has more digits to the right of the decimal separator than there are zeros to the right of the decimal separator in the format expression, round the number to as many decimal places as there are zeros. If the number has more digits to the left of the decimal separator than there are zeros to the left of the decimal separator in the format expression, display the extra digits without modification.|
|(**#**)|Digit placeholder. Display a digit or nothing. If the expression has a digit in the position where the # appears in the format string, display it; otherwise, display nothing in that position. This symbol works like the 0 digit placeholder, except that leading and trailing zeros aren't displayed if the number has the same or fewer digits than there are # characters on either side of the decimal separator in the format expression.|
|(**.**)|Decimal placeholder. In some locales, a comma is used as the decimal separator. The decimal placeholder determines how many digits are displayed to the left and right of the decimal separator. If the format expression contains only number signs to the left of this symbol, numbers smaller than 1 begin with a decimal separator. To display a leading zero displayed with fractional numbers, use 0 as the first digit placeholder to the left of the decimal separator. The actual character used as a decimal placeholder in the formatted output depends on the Number Format recognized by your system.|
|(**%)**|Percentage placeholder. The expression is multiplied by 100. The percent character (**%**) is inserted in the position where it appears in the format string.|
|(**,**)|Thousand separator. In some locales, a period is used as a thousand separator. The thousand separator separates thousands from hundreds within a number that has four or more places to the left of the decimal separator. Standard use of the thousand separator is specified if the format contains a thousand separator surrounded by digit placeholders (**0** or **#**). Two adjacent thousand separators or a thousand separator immediately to the left of the decimal separator (whether or not a decimal is specified) means "scale the number by dividing it by 1000, rounding as needed." For example, you can use the format string "##0,," to represent 100 million as 100. Numbers smaller than 1 million are displayed as 0. Two adjacent thousand separators in any position other than immediately to the left of the decimal separator are treated simply as specifying the use of a thousand separator. The actual character used as the thousand separator in the formatted output depends on the Number Format recognized by your system.|
|(**:**)|Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by your system settings.|
|(**/**)|Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by your system settings.|
|(**E- E+ e- e+**)|Scientific format. If the format expression contains at least one digit placeholder (**0** or **#**) to the right of E-, E+, e-, or e+, the number is displayed in scientific format and E or e is inserted between the number and its exponent. The number of digit placeholders to the right determines the number of digits in the exponent. Use E- or e- to place a minus sign next to negative exponents. Use E+ or e+ to place a minus sign next to negative exponents and a plus sign next to positive exponents.|
|**- + $** ( )|Display a literal character. To display a character other than one of those listed, precede it with a backslash (`\`) or enclose it in double quotation marks (" ").|
|(**\\**)|Display the next character in the format string. To display a character that has special meaning as a literal character, precede it with a backslash (`\`). The backslash itself isn't displayed. Using a backslash is the same as enclosing the next character in double quotation marks. To display a backslash, use two backslashes (`\\`). Examples of characters that can't be displayed as literal characters are the date-formatting and time-formatting characters (a, c, d, h, m, n, p, q, s, t, w, y, /, and :), the numeric-formatting characters (#, 0, %, E, e, comma, and period), and the string-formatting characters (@, &, <, >, and !).|
|("ABC")|Display the string inside the double quotation marks (" ").|

## Remarks

If you include semicolons with nothing between them, the missing section is shown using the format of the positive value.  
  
## See also

[FORMAT function](format-function-dax.md)  
[Pre-Defined Numeric Formats for the FORMAT function](pre-defined-numeric-formats-for-the-format-function.md)  
[Custom date and time formats for the FORMAT function](custom-date-and-time-formats-for-the-format-function.md)  
