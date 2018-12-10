---
title: "EOMONTH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# EOMONTH
Returns the date in **datetime** format of the last day of the month, before or after a specified number of months. Use EOMONTH to calculate maturity dates or due dates that fall on the last day of the month.  
  
## Syntax  
  
```dax
EOMONTH(<start_date>, <months>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|start_date|The start date in **datetime** format, or in an accepted text representation of a date.|  
|months|A number representing the number of months before or after the **start_date**. **Note:** If you enter a number that is not an integer, the number is rounded up or down to the nearest integer.|  
  
## Return value  
A date (**datetime**).  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as sequential serial numbers, DAX works with dates in a **datetime** format. The EOMONTH function can accept dates in other formats, with the following restrictions:  
  
If **start_date** is not a valid date, EOMONTH returns an error.  
  
If **start_date** is a numeric value that is not in a **datetime** format, EOMONTH will convert the number to a date. To avoid unexpected results, convert the number to a **datetime** format before using the EOMONTH function.  
  
If **start_date** plus months yields an invalid date, EOMONTH returns an error. Dates before March 1st of 1900 and after December 31st of 9999 are invalid.  
  
When the date argument is a text representation of the date, the EDATE function uses the locale and date time settings, of the client computer, to understand the text value in order to perform the conversion. If current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009. However, if the current date time settings represent a date in the format of Day/Month/Year, the same string would be interpreted as a datetime value equivalent to August 1st of 2009.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following expression returns May 31, 2008, because the **months** argument is rounded to 2.  
  
```dax
=EOMONTH("March 3, 2008",1.5)  
```
  
## See also  
[EDATE function &#40;DAX&#41;](edate-function-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
  
