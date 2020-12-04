---
title: "FORMAT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/04/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# FORMAT

Converts a value to text according to the specified format.

## Syntax

```dax
FORMAT(<value>, <format_string>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|value|A value or expression that evaluates to a single value.|
|format_string|A string with the formatting template.|

## Return value

A string containing **value** formatted as defined by **format_string**.

> [!NOTE]
> If **value** is BLANK the function returns an empty string.
>
> If **format_string** is BLANK, the value is formatted with a "General Number" or "General Date" format (according to **value** data type).

## Remarks

- All predefined formatting strings use the current user locale when formatting the result.

- The format strings supported as an argument to the DAX FORMAT function are based on the format strings used by Visual Basic (OLE Automation), not on the format strings used by the .NET Framework. Therefore, you might get unexpected results or an error if the argument doesn't match any defined format strings. For example, "p" as an abbreviation for "Percent" isn't supported. Strings that you provide as an argument to the FORMAT function that aren't included in the list of predefined format strings are handled as part of a custom format string, or as a string literal.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Predefined numeric formats

The following predefined numeric formats can be specified in the **format_string** argument:  
  
|Format|Description|  
|------------------------|---------------|  
|`"General Number"`|Displays number with no thousand separators.|  
|`"Currency"`|Displays number with thousand separators, if appropriate; displays two digits to the right of the decimal separator. Output is based on system locale settings.|  
|`"Fixed"`|Displays at least one digit to the left and two digits to the right of the decimal separator.|  
|`"Standard"`|Displays number with thousand separators, at least one digit to the left and two digits to the right of the decimal separator.|  
|`"Percent"`|Displays number multiplied by 100 with a percent sign (%) appended immediately to the right; always displays two digits to the right of the decimal separator.|  
|`"Scientific"`|Uses standard scientific notation, providing two significant digits.|  
|`"Yes/No"`|Displays No if number is 0; otherwise, displays Yes.|  
|`"True/False"`|Displays False if number is 0; otherwise, displays True.|  
|`"On/Off"`|Displays Off if number is 0; otherwise, displays On.|   

## Custom numeric formats

A custom format expression for numbers can have from one to three sections separated by semicolons. If the format string argument contains one of the named numeric formats, only one section is allowed.

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
"$#,##0"
```

If you include semicolons with nothing between them, the missing section is shown using the format of the positive value.

### Custom numeric format characters

The following custom numeric format characters can be specified in the **format_string** argument:  

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

## Predefined date and time formats

The following predefined date and time formats can be specified in the **format_string** argument. When using formats other than these, they are interpreted as a custom date/time format:

|Format|Description|
|------------------------|---------------|
|`"General Date"`|Displays a date and/or time. For example, 3/12/2008 11:07:31 AM. Date display is determined by your application's current culture value.|
|`"Long Date"` or `"Medium Date"`|Displays a date according to your current culture's long date format. For example, Wednesday, March 12, 2008.|
|`"Short Date"`|Displays a date using your current culture's short date format. For example, 3/12/2008.|  
|`"Long Time"` or|Displays a time using your current culture's long time format; typically includes hours, minutes, seconds. For example, 11:07:31 AM.|
|`"Medium Time"`|Displays a time in 12 hour format. For example, 11:07 AM.|
|`"Short Time"`|Displays a time in 24 hour format. For example, 11:07.|

## Custom date and time formats

The following tables describe characters used to create custom date/time formats:

The following custom date/time format characters can be specified in the **format_string** to create custom date/time formats:

|Character|Description|
|:-----|:-----|
|(**:**)|Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by your system settings.|
|(**/**)|Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by your system settings.|
|(**&#x5c;**)|Backslash. Displays the next character as a literal character. So, it's not interpreted as a formatting character.|
|(**"**)|Double quote. Text enclosed within double quotes is displayed. So, it's not interpreted as formatting characters.|
|c|Display the date as `ddddd` and display the time as `ttttt`, in that order. Display only date information if there is no fractional part to the date serial number; display only time information if there is no integer portion.|
|d|Display the day as a number without a leading zero (1-31).|
|dd|Display the day as a number with a leading zero (01-31).|
|ddd|Display the day as an abbreviation (Sun-Sat). Localized.|
|dddd|Display the day as a full name (Sunday-Saturday). Localized.|
|ddddd|Display the date as a complete date (including day, month, and year), formatted according to your system's short date format setting. The default short date format is  `mm/dd/yyyy`.|
|dddddd|Display a date serial number as a complete date (including day, month, and year) formatted according to the long date setting recognized by your system. The default long date format is  `dddd, mmmm d, yyyy`.|
|w|Display the day of the week as a number (1 for Sunday through 7 for Saturday).|
|ww|Display the week of the year as a number (1-54).|
|m|Display the month as a number without a leading zero (1-12). If `m` immediately follows `h` or `hh`, minute rather than the month is displayed.|
|mm|Display the month as a number with a leading zero (01-12). If `mm` immediately follows `h` or `hh`, minute rather than the month is displayed. |
|mmm|Display the month as an abbreviation (Jan-Dec). Localized.|
|mmmm|Display the month as a full month name (January-December). Localized.|
|q|Display the quarter of the year as a number (1-4).|
|y|Display the day of the year as a number (1-366).|
|yy|Display the year as a 2-digit number (00-99).|
|yyyy|Display the year as a 4-digit number (100-9999).|
|h|Display the hour as a number without a leading zero (0-23).|
|hh|Display the hour as a number with a leading zero (00-23).|
|n|Display the minute as a number without a leading zero (0-59).|
|nn|Display the minute as a number with a leading zero (00-59).|
|s|Display the second as a number without a leading zero (0-59).|
|ss|Display the second as a number with a leading zero (00-59).|
|ttttt|Display a time as a complete time (including hour, minute, and second), formatted using the time separator defined by the time format recognized by your system. A leading zero is displayed if the leading zero option is selected and the time is before 10:00 A.M. or P.M. The default time format is `h:mm:ss`.|
|AM/PM|Use the 12-hour clock and display an uppercase AM with any hour before noon; display an uppercase PM with any hour between noon and 11:59 P.M.|
|am/pm|Use the 12-hour clock and display a lowercase AM with any hour before noon; display a lowercase PM with any hour between noon and 11:59 P.M.|
|A/P|Use the 12-hour clock and display an uppercase A with any hour before noon; display an uppercase P with any hour between noon and 11:59 P.M.|
|a/p|Use the 12-hour clock and display a lowercase A with any hour before noon; display a lowercase P with any hour between noon and 11:59 P.M.|
|AMPM|Use the 12-hour clock and display the AM string literal as defined by your system with any hour before noon; display the PM string literal as defined by your system with any hour between noon and 11:59 P.M. AMPM can be either uppercase or lowercase, but the case of the string displayed matches the string as defined by your system settings. The default format is AM/PM. If your system is set to 24-hour clock, the string is typical set to an empty string.|

Date/time formatting uses the current user locale to format the string. For example, consider the date June 25, 2020. When it's formatted using format string "m/d/yyyy" it will be:

- User locale is United States of America (en-US): "6/25/2020"
- User locale is Germany (de-DE): "6.25.2020"

### Custom date and time format examples

The following examples use the date/time Thursday, June 25, 2020, at 1:23:45 PM. Germany (de-DE) uses a 24-hour system. There's no equivalent of AM/PM.

|Format|Result (en-US)|Result (de-DE)|
|-------------|--------------|--------------|
|`"c"`|06/25/2020 13:23:45|25.06.2020 13:23:45|
|`"d"`|25|25|
|`"dd"`|25|25|
|`"ddd"`|Thu|Do|
|`"dddd"`|Thursday|Donnerstag|
|`"ddddd"`|06/25/2020|25.06.2020|
|`"dddddd"`|Thursday, June 25, 2020|Donnerstag, 25. Juni 2020|
|`"w"`|5|5|
|`"ww"`|26|26|
|`"m"`|6|6|
|`"mm"`|06|06|
|`"mmm"`|Jun|Jun|
|`"mmmm"`|June|Juni|
|`"q"`|2|2|
|`"y"`|177|177|
|`"yy"`|20|20|
|`"yyyy"`|2020|2020|
|`"""Year"" yyyy"`|Year 2020|Year 2020|
|`"yyyy \Qq"`|2020 Q2|2020 Q2|
|`"dd/mm/yyyy"`|25/06/2020|25.06.2020|
|`"mm/dd/yyyy"`|06/25/2020|06.25.2020|
|`"h:nn:ss"`|13:23:45|13:23:45|
|`"h:nn:ss AMPM"`|1:23:45 PM|1:23:45|
|`"hh:nn:ss"`|13:23:45|13:23:45|
|`"hh:nn:ss AMPM"`|01:23:45 PM|01:23:45|
|`"ttttt"`|13:23:45|13:23:45|
|`"ttttt AMPM"`|13:23:45 PM|13:23:45|
|`"mm/dd/yyyy hh:nn:ss AMPM"`|06/25/2020 01:23:45 PM|6.25.2020 01:23:45|

## Examples

```dax
= FORMAT( 12345.67, "General Number")  
= FORMAT( 12345.67, "Currency")  
= FORMAT( 12345.67, "Fixed")  
= FORMAT( 12345.67, "Standard")  
= FORMAT( 12345.67, "Percent")  
= FORMAT( 12345.67, "Scientific")
```

Returns the following:  

**12345.67** "General Number" displays the number with no formatting.  
  
**$12,345.67** "Currency" displays the number with your currency locale formatting. The sample here shows the default United States currency formatting.  
  
**12345.67** "Fixed" displays at least one digit to the left of the decimal separator and two digits to the right of the decimal separator.  
  
**12,345.67** "Standard" displays at least one digit to the left of the decimal separator and two digits to the right of the decimal separator, and includes thousand separators. The sample here shows the default United States number formatting.  
  
**1,234,567.00 %** "Percent" displays the number as a percentage (multiplied by 100) with formatting and the percent sign at the right of the number separated by a single space.  
  
**1.23E+04** "Scientific" displays the number in scientific notation with two decimal digits.
