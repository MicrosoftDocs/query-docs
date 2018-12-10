---
title: "Pre-Defined Numeric Formats for the FORMAT function | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Pre-Defined Numeric Formats for the FORMAT function
The following table identifies the predefined numeric format names. These may be used by name as the style argument for the Format function.  
  
|Format specification|Description|  
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
  
## Remarks  
Note that format strings are based on Visual Basic (OLE Automation) and therefore might have slightly different behavior than the format strings used by the .NET Framework. Abbreviations such as “P” and “x” are not supported. Any other strings that you provide as an argument to the FORMAT function are interpreted as defining a custom format.  
  
> [!IMPORTANT]  
> If *value* is BLANK() the function returns an empty string.  
>   
> If *format_string* is BLANK(), the value is formatted with a "General Number" format.  
  
## Example  
The following samples show the usage of different predefined formatting strings to format a numeric value.  
  
```dax
FORMAT( 12345.67, "General Number")  
FORMAT( 12345.67, "Currency")  
FORMAT( 12345.67, "Fixed")  
FORMAT( 12345.67, "Standard")  
FORMAT( 12345.67, "Percent")  
FORMAT( 12345.67, "Scientific")  
```

The above expressions return the following results:  
  
**12345.67** "General Number" displays the number with no formatting.  
  
**$12,345.67** "Currency" displays the number with your currency locale formatting. The sample here shows the default United States currency formatting.  
  
**12345.67** "Fixed" displays at least one digit to the left of the decimal separator and two digits to the right of the decimal separator.  
  
**12,345.67** " Standard " displays at least one digit to the left of the decimal separator and two digits to the right of the decimal separator, and includes thousand separators. The sample here shows the default United States number formatting.  
  
**1,234,567.00 %** "Percent" displays the number as a percentage (multiplied by 100) with formatting and the percent sign at the right of the number separated by a single space.  
  
**1.23E+04** "Scientific" displays the number in scientific notation with two decimal digits.  
  
## See also  
[FORMAT function &#40;DAX&#41;](format-function-dax.md)  
[Pre-defined date and time formats for the FORMAT function](pre-defined-date-and-time-formats-for-the-format-function.md)  
[Custom Numeric Formats for the FORMAT function](custom-numeric-formats-for-the-format-function.md)  
  
