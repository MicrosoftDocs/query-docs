---
title: "Pre-defined date and time formats for the FORMAT function | Microsoft Docs"
ms.service: powerbi 
ms.date: 06/30/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Pre-defined date and time formats for the FORMAT function

The following table identifies the predefined date and time format names. If you use strings other than these predefined strings, they will be interpreted as a custom date and time format.

|Format specification|Description|
|------------------------|---------------|
|`"General Date"`|Displays a date and/or time. For example, 3/12/2008 11:07:31 AM. Date display is determined by your application's current culture value.|
|`"Long Date"` or `"Medium Date"`|Displays a date according to your current culture's long date format. For example, Wednesday, March 12, 2008.|
|`"Short Date"`|Displays a date using your current culture's short date format. For example, 3/12/2008.|  
|`"Long Time"` or|Displays a time using your current culture's long time format; typically includes hours, minutes, seconds. For example, 11:07:31 AM.|
|`"Medium Time"`|Displays a time in 12 hour format. For example, 11:07 AM.|
|`"Short Time"`|Displays a time in 24 hour format. For example, 11:07.|

## Remarks

Format strings are based on Visual Basic (OLE Automation) and not the .NET Framework formatting strings. Therefore, your results might be slightly different than what you expect from .NET format strings. Note that abbreviations such as "D" for Long Date and "t" for Short Time aren't supported.

> [!IMPORTANT]
> If *value* is BLANK the function returns an empty string.
>
> If *format_string* is BLANK, the value is formatted with the "General Date" format.

## See also

- [FORMAT function (DAX)](format-function-dax.md)
- [Custom date and time formats for the FORMAT function](custom-date-and-time-formats-for-the-format-function.md)  
