---
title: "WEEKDAY Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# WEEKDAY Function (DAX)
Returns a number from 1 to 7 identifying the day of the week of a date. By default the day ranges from 1 (Sunday) to 7 (Saturday).  
  
## Syntax  
  
```  
WEEKDAY(<date>, <return_type>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|A date in **datetime** format.<br /><br />Dates should be entered by using the DATE function, by using expressions that result in a date, or as the result of other formulas.|  
|**return_type**|A number that determines the return value:<br /><br />Return type: **1**, week begins on Sunday (1) and ends on Saturday (7). numbered 1 through 7.<br /><br />Return type: **2**, week begins on Monday (1) and ends on Sunday (7).<br /><br />Return type: **3**, week begins on Monday (0) and ends on Sunday (6).numbered 1 through 7.|  
  
## Return Value  
An integer number from 1 to 7.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX works with dates and times in a **datetime** format. If you need to display dates as serial numbers, you can use the formatting options in Excel.  
  
You can also type dates in an accepted text representation of a date, but to avoid unexpected results, it is best to convert the text date to a **datetime** format first.  
  
When the date argument is a text representation of the date, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. If the current date/time settings represent dates in the format of Month/Day/Year, then the string, "1/8/2009", is interpreted as a **datetime** value equivalent to January 8th of 2009. However, if the current date/time settings represent dates in the format of Day/Month/Year, then the same string would be interpreted as a **datetime** value equivalent to August 1st of 2009.  
  
## Example  
The following example gets the date from the [HireDate] column, adds 1, and displays the weekday corresponding to that date. Because the **return_type** argument has been omitted, the default format is used, in which 1 is Sunday and 7 is Saturday. If the result is 4, the day would be Wednesday.  
  
```  
=WEEKDAY([HireDate]+1)  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[WEEKNUM Function &#40;DAX&#41;](weeknum-function-dax.md)  
[YEARFRAC Function &#40;DAX&#41;](yearfrac-function-dax.md)  
  
