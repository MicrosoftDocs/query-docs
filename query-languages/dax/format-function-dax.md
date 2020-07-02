---
title: "FORMAT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/17/2019
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
  
> [!IMPORTANT]  
> If *value* is BLANK() the function returns an empty string.  
>   
> If *format_string* is BLANK(), the value is formatted with a "General Number" or "General Date" format (according to **value** type).  
  
## Remarks  
For information on how to use the **format_string** parameter, see the appropriate topic listed below:  
  
|To Format|Follow these instructions|  
|-------------|-----------------------------|  
|Numbers|Use predefined numeric formats or create user-defined numeric formats.|  
|Dates and times|Use predefined date/time formats or create user-defined date/time formats.|  
  
All predefined formatting strings use the current user locale when formatting the result.  
  
> [!CAUTION]  
> The format strings supported as an argument to the DAX FORMAT function are based on the format strings used by Visual Basic (OLE Automation), not on the format strings used by the .NET Framework. Therefore, you might get unexpected results or an error if the argument does not match any defined format strings. For example, “p” as an abbreviation for “Percent” is not supported. Strings that you provide as an argument to the FORMAT function that are not included in the list of predefined format strings are handled as part of a custom format string, or as a string literal.  
  
This function is not optimized for use in DirectQuery mode. To learn more, see  [DAX formula compatibility in DirectQuery mode](https://go.microsoft.com/fwlink/?LinkId=219172).   
  
## See also  
[Pre-Defined Numeric Formats for the FORMAT function](pre-defined-numeric-formats-for-the-format-function.md)  
[Custom Numeric Formats for the FORMAT function](custom-numeric-formats-for-the-format-function.md)  
[Pre-defined date and time formats for the FORMAT function](pre-defined-date-and-time-formats-for-the-format-function.md)  
[Custom date and time formats for the FORMAT function](custom-date-and-time-formats-for-the-format-function.md)  
[VALUE function &#40;DAX&#41;](value-function-dax.md)  
  
