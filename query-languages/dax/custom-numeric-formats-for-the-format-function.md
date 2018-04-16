---
title: "Custom Numeric Formats for the FORMAT Function | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Custom Numeric Formats for the FORMAT Function
A user-defined format expression for numbers can have from one to three sections separated by semicolons. If the Style argument of the Format function contains one of the predefined numeric formats, only one section is allowed.  
  
|If you use|This is the result|  
|--------------|----------------------|  
|One section only|The format expression applies to all values.|  
|Two sections|The first section applies to positive values and zeros; the second applies to negative values.|  
|Three sections|The first section applies to positive values, the second applies to negative values, and the third applies to zeros.|  
  
## Format Specifications  
The following table identifies characters you can use to create user-defined number formats.  
  
|Format specification|Description|  
|------------------------|---------------|  
|None|Displays the number with no formatting.|  
|**0** (zero character)|Digit placeholder. Displays a digit or a zero. If the expression has a digit in the position where the zero appears in the format string, displays the digit; otherwise, displays a zero in that position.<br /><br />If the number has fewer digits than there are zeros (on either side of the decimal) in the format expression, displays leading or trailing zeros. If the number has more digits to the right of the decimal separator than there are zeros to the right of the decimal separator in the format expression, rounds the number to as many decimal places as there are zeros. If the number has more digits to the left of the decimal separator than there are zeros to the left of the decimal separator in the format expression, displays the extra digits without modification.|  
|**#**|Digit placeholder. Displays a digit or nothing. If the expression has a digit in the position where the # character appears in the format string, displays the digit; otherwise, displays nothing in that position.<br /><br />This symbol works like the 0 digit placeholder, except that leading and trailing zeros aren't displayed if the number has fewer digits than there are # characters on either side of the decimal separator in the format expression.|  
|**.** (dot character)|Decimal placeholder. The decimal placeholder determines how many digits are displayed to the left and right of the decimal separator. If the format expression contains only # characters to the left of this symbol; numbers smaller than 1 begin with a decimal separator. To display a leading zero displayed with fractional numbers, use zero as the first digit placeholder to the left of the decimal separator. In some locales, a comma is used as the decimal separator. The actual character used as a decimal placeholder in the formatted output depends on the number format recognized by your system. Thus, you should use the period as the decimal placeholder in your formats even if you are in a locale that uses a comma as a decimal placeholder. The formatted string will appear in the format correct for the locale.|  
|**%**|Percent placeholder. Multiplies the expression by 100. The percent character (%) is inserted in the position where it appears in the format string.|  
|**,** (comma character)|Thousand separator. The thousand separator separates thousands from hundreds within a number that has four or more places to the left of the decimal separator. Standard use of the thousand separator is specified if the format contains a thousand separator surrounded by digit placeholders (0 or #).<br /><br />A thousand separator immediately to the left of the decimal separator (whether or not a decimal is specified) or as the rightmost character in the string means "scale the number by dividing it by 1,000, rounding as needed." Numbers smaller than 1,000 but greater or equal to 500 are displayed as 1, and numbers smaller than 500 are displayed as 0. Two adjacent thousand separators in this position scale by a factor of 1 million, and an additional factor of 1,000 for each additional separator.<br /><br />Multiple separators in any position other than immediately to the left of the decimal separator or the rightmost position in the string are treated simply as specifying the use of a thousand separator. In some locales, a period is used as a thousand separator. The actual character used as the thousand separator in the formatted output depends on the Number Format recognized by your system. Thus, you should use the comma as the thousand separator in your formats even if you are in a locale that uses a period as a thousand separator. The formatted string will appear in the format correct for the locale.<br /><br />For example, consider the three following format strings:<br /><br />"#,0.", which uses the thousands separator to format the number 100 million as the string "100,000,000".<br /><br />"#0,.", which uses scaling by a factor of one thousand to format the number 100 million as the string "100000".<br /><br />"#,0,.", which uses the thousands separator and scaling by one thousand to format the number 100 million as the string "100,000".|  
|**:** (colon character)|Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by your system settings.|  
|**/** (forward slash character)|Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by your system settings.|  
|**E-** , **E+** , **e-** , **e+**|Scientific format. If the format expression contains at least one digit placeholder (0 or #) to the left of E-, E+, e-, or e+, the number is displayed in scientific format and E or e is inserted between the number and its exponent. The number of digit placeholders to the left determines the number of digits in the exponent. Use E- or e- to place a minus sign next to negative exponents. Use E+ or e+ to place a minus sign next to negative exponents and a plus sign next to positive exponents. You must also include digit placeholders to the right of this symbol to get correct formatting.|  
|**-+$()**|Literal characters. These characters are displayed exactly as typed in the format string. To display a character other than one of those listed, precede it with a backslash (\\) or enclose it in double quotation marks (" ").|  
|**\\** (backward slash character)|Displays the next character in the format string. To display a character that has special meaning as a literal character, precede it with a backslash (\\). The backslash itself isn't displayed. Using a backslash is the same as enclosing the next character in double quotation marks. To display a backslash, use two backslashes.<br /><br />Examples of characters that can't be displayed as literal characters are the date-formatting and time-formatting characters (a, c, d, h, m, n, p, q, s, t, w, y, /, and :), the numeric-formatting characters (#, 0, %, E, e, comma, and period), and the string-formatting characters (@, &amp;, &lt;, &gt;, and !).|  
|**"**ABC**"**|Displays the string inside the double quotation marks (" "). To include a string in the style argument from within code, you must use Chr(34) to enclose the text (34 is the character code for a quotation mark (")).|  
  
The following table contains some sample format expressions for numbers. (These examples all assume that your system's locale setting is English-U.S.) The first column contains the format strings for the Format function; the other columns contain the resulting output if the formatted data has the value given in the column headings.  
  
|Format (Style)|"5" formatted as|"-5" formatted as|"0.5" formatted as|"0" formatted as|  
|------------------|--------------------|----------------------|----------------------|--------------------|  
|Zero-length string ("")|5|-5|0.5|0|  
|0|5|-5|1|0|  
|0.00|5.00|-5.00|0.50|0.00|  
|#,##0|5|-5|1|0|  
|$#,##0;($#,##0)|$5|($5)|$1|$0|  
|$#,##0.00;($#,##0.00)|$5.00|($5.00)|$0.50|$0.00|  
|0%|500%|-500%|50%|0%|  
|0.00%|500.00%|-500.00%|50.00%|0.00%|  
|0.00E+00|5.00E+00|-5.00E+00|5.00E-01|0.00E+00|  
|0.00E-00|5.00E00|-5.00E00|5.00E-01|0.00E00|  
|"$#,##0;;\Z\e\r\o"|$5|$-5|$1|Zero|  
  
## Remarks  
If you include semicolons with nothing between them, the missing section is printed using the format of the positive value.  
  
## See Also  
[FORMAT Function &#40;DAX&#41;](format-function-dax.md)  
[Pre-Defined Numeric Formats for the FORMAT Function](pre-defined-numeric-formats-for-the-format-function.md)  
[Custom Date and Time formats for the FORMAT Function](custom-date-and-time-formats-for-the-format-function.md)  
  
