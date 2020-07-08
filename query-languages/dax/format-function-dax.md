---
title: "FORMAT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/06/2020
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

- For information on how to use the **format_string** parameter, see the appropriate topic listed below:

    |To format|Follow these instructions|
    |-------------|-----------------------------|
    |Numbers|Use [predefined numeric formats](pre-defined-numeric-formats-for-the-format-function.md) or create [user-defined numeric formats](custom-numeric-formats-for-the-format-function.md).|
    |Dates and times|Use [predefined date/time formats](pre-defined-date-and-time-formats-for-the-format-function.md) or create [user-defined date/time formats](custom-date-and-time-formats-for-the-format-function.md).|

- All predefined formatting strings use the current user locale when formatting the result.

    > [!CAUTION]  
    > The format strings supported as an argument to the DAX FORMAT function are based on the format strings used by Visual Basic (OLE Automation), not on the format strings used by the .NET Framework. Therefore, you might get unexpected results or an error if the argument doesn't match any defined format strings. For example, "p" as an abbreviation for "Percent" isn't supported. Strings that you provide as an argument to the FORMAT function that aren't included in the list of predefined format strings are handled as part of a custom format string, or as a string literal.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

|Formula|Description|Result|
|-----------|---------------|----------|
|= FORMAT(SUM(Sales[Sales Amount]), "Currency")|Formats the number using a pre-defined format|$1,234.56 (for en-US locale)|
|= FORMAT(SUM(Sales[Sales Amount]), "$#,##0")|Formats the number using a custom format|$1,234|
|= FORMAT('Date'[Date], "Short Date")|Formats the date using a pre-defined format|06/25/2020 (for en-US locale)|
|= FORMAT('Date'[Date], "dd/mm/yyyy")|Formats the date using a custom format|25/06/2020|

## See also

[Pre-Defined Numeric Formats for the FORMAT function]    (pre-defined-numeric-formats-for-the-format-function.md)  
[Custom Numeric Formats for the FORMAT function](custom-numeric-formats-for-the-format-function.md)  
[Pre-defined date and time formats for the FORMAT function](pre-defined-date-and-time-formats-for-the-format-function.md)  
[Custom date and time formats for the FORMAT function](custom-date-and-time-formats-for-the-format-function.md)  
[VALUE function (DAX)](value-function-dax.md)  
[Text functions](text-functions-dax.md)  
