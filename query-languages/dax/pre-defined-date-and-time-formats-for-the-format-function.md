---
title: "Pre-defined Date and Time formats for the FORMAT Function | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Pre-defined Date and Time formats for the FORMAT Function
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
The formatting strings are based on Visual Basic (OLE Automation) and not the .NET Framework formatting strings; therefore, your results might be slightly different than what you expect from .NET format strings. Note that abbreviations such as “D” for Long Date and “t” for Short Time are not supported.  
  
> [!IMPORTANT]  
> If *value* is BLANK() the function returns an empty string.  
>   
> If *format_string* is BLANK(), the value is formatted with a "General Date" format.  
  
## See Also  
[Custom Date and Time formats for the FORMAT Function](custom-date-and-time-formats-for-the-format-function.md)  
  
