---
title: "EDATE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# EDATE

Returns the date that is the indicated number of months before or after the start date. Use EDATE to calculate maturity dates or due dates that fall on the same day of the month as the date of issue.  
  
## Syntax  
  
```dax
EDATE(<start_date>, <months>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|start_date|A date in **datetime** or **text** format that represents the start date.|  
|months|An integer that represents the number of months before or after **start_date**.|  
  
## Return value

A date (**datetime**).  
  
## Remarks

- In contrast to Microsoft Excel, which stores dates as sequential serial numbers, DAX works with dates in a **datetime** format. Dates stored in other formats are converted implicitly.  
  
- If **start_date** is not a valid date, EDATE returns an error. Make sure that the column reference or date that you supply as the first argument is a date.  
  
- If **months** is not an integer, it is truncated.  
  
- When the date argument is a text representation of the date, the EDATE function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. If the current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009. However, if the current date time settings represent a date in the format of Day/Month/Year, the same string would be interpreted as a datetime value equivalent to August 1st of 2009.  
  
- If the requested date is past the last day of the corresponding month, then the last day of the month is returned. For example, the following functions: EDATE("2009-01-29", 1), EDATE("2009-01-30", 1), EDATE("2009-01-31", 1) return February 28th of 2009; that corresponds to one month after the start date.  
  
- This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [https://go.microsoft.com/fwlink/?LinkId=219171](https://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example

The following example returns the date three months after the order date, which is stored in the column [TransactionDate].  
  
```dax
= EDATE([TransactionDate],3)  
```
  
## See also

[EOMONTH function &#40;DAX&#41;](eomonth-function-dax.md)  
[Date and time functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
