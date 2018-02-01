---
title: "FORMAT Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.FORMAT.f1"
helpviewer_keywords: 
  - "FORMAT function"
ms.assetid: e14f430d-3c3a-46bd-911f-f4e2d6d0a9b6
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# FORMAT Function (DAX)
Converts a value to text according to the specified format.  
  
## Syntax  
  
```  
FORMAT(<value>, <format_string>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**value**|A value or expression that evaluates to a single value.|  
|**format_string**|A string with the formatting template.|  
  
## Return Value  
A string containing **value** formatted as defined by **format_string**.  
  
> [!IMPORTANT]  
> If *value* is BLANK() the function returns an empty string.  
>   
> If *format_string* is BLANK(), the value is formatted with a "General Number" or "General Date" format (according to **value** type).  
  
## Remarks  
For information on how to use the **format_string** parameter, see the appropriate topic listed below:  
  
|To Format|Follow these instructions|  
|-------------|-----------------------------|  
|Numbers|Use [predefined numeric formats](http://msdn.microsoft.com/en-us/78e0ac9e-9e3a-45dd-991f-599a206b8c65) or create [user-defined numeric formats](http://msdn.microsoft.com/en-us/0432d01e-d0b5-49a0-b93e-fb636e0a8274).|  
|Dates and times|Use [predefined date/time formats](http://msdn.microsoft.com/en-us/b37f6d2f-1f73-4daa-8e64-df475a3622b8) or create [user-defined date/time formats](http://msdn.microsoft.com/en-us/4dd49f41-05fe-474d-8678-31fe5f86a137).|  
  
All predefined formatting strings use the current user locale when formatting the result.  
  
> [!CAUTION]  
> The format strings supported as an argument to the DAX FORMAT function are based on the format strings used by Visual Basic (OLE Automation), not on the format strings used by the .NET Framework. Therefore, you might get unexpected results or an error if the argument does not match any defined format strings. For example, “p” as an abbreviation for “Percent” is not supported. Strings that you provide as an argument to the FORMAT function that are not included in the list of predefined format strings are handled as part of a custom format string, or as a string literal.  
  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## See Also  
[Pre-Defined Numeric Formats for the FORMAT Function](pre-defined-numeric-formats-for-the-format-function.md)  
[Custom Numeric Formats for the FORMAT Function](custom-numeric-formats-for-the-format-function.md)  
[Pre-defined Date and Time formats for the FORMAT Function](pre-defined-date-and-time-formats-for-the-format-function.md)  
[Custom Date and Time formats for the FORMAT Function](custom-date-and-time-formats-for-the-format-function.md)  
[VALUE Function &#40;DAX&#41;](value-function-dax.md)  
  
