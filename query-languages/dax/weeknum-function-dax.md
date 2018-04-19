---
title: "WEEKNUM Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# WEEKNUM Function (DAX)
Returns the week number for the given date and year according to the **return_type** value. The week number indicates where the week falls numerically within a year.  
  
## Syntax  
  
```  
WEEKNUM(<date>, <return_type>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|The date in **datetime** format.|  
|**return_type**|A number that determines the return value: use 1 when the week begins on Sunday; use 2 when the week begins on Monday. The default is 1.<br /><br />Return type: **1**, week begins on Sunday. Weekdays are numbered 1 through 7.<br /><br />Return type: **2**, week begins on Monday. Weekdays are numbered 1 through 7.|  
  
## Return Value  
An integer number.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** data type to work with dates and times. If the source data is in a different format, DAX implicitly converts the data to **datetime** to perform calculations.  
  
By default, the WEEKNUM function uses a calendar convention in which the week containing January 1 is considered to be the first week of the year. However, the ISO 8601 calendar standard, widely used in Europe, defines the first week as the one with the majority of days (four or more) falling in the new year. This means that for years in which there are three days or less in the first week of January, the WEEKNUM function returns week numbers that are different from the ISO 8601 definition.  
  
## Example  
The following example returns the week number of the date February 14, 2010.  
  
```  
=WEEKNUM("Feb 14, 2010", 2)  
```  
  
## Example  
The following example returns the week number of the date stored in the column, **HireDate**, from the table, **Employees**.  
  
```  
=WEEKNUM('Employees'[HireDate])  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[YEARFRAC Function &#40;DAX&#41;](yearfrac-function-dax.md)  
[WEEKDAY Function &#40;DAX&#41;](weekday-function-dax.md)  
  
