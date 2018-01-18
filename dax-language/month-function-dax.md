---
title: "MONTH Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.MONTH.f1"
helpviewer_keywords: 
  - "MONTH function"
ms.assetid: df79a8ca-ea68-4991-ba47-5fee6f6c937e
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# MONTH Function (DAX)
Returns the month as a number from 1 (January) to 12 (December).  
  
## Syntax  
  
```  
MONTH(<datetime>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**date**|A date in **datetime** or text format.|  
  
## Return Value  
An integer number from 1 to 12.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** format when working with dates. You can enter the date used as argument to the MONTH function by typing an accepted **datetime** format, by providing a reference to a column that contains dates, or by using an expression that returns a date.  
  
Values returned by the YEAR, MONTH and DAY functions will be Gregorian values regardless of the display format for the supplied date value. For example, if the display format of the supplied date is Hijri, the returned values for the YEAR, MONTH and DAY functions will be values associated with the equivalent Gregorian date.  
  
When the date argument is a text representation of the date, the function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. If the current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009, and the function yields a result of 1. However, if the current date time settings represent a date in the format of Day/Month/Year, then the same string would be interpreted as a datetime value equivalent to August 1st of 2009, and the function yields a result of 8.  
  
If the text representation of the date cannot be correctly converted to a datetime value, the function returns an error.  
  
## Example  
The following expression returns 3, which is the integer corresponding to March, the month in the **date** argument.  
  
```  
=MONTH("March 3, 2008 3:45 PM")  
```  
  
## Example  
The following expression returns the month from the date in the **TransactionDate** column of the **Orders** table.  
  
```  
=MONTH(Orders[TransactionDate])  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[HOUR Function &#40;DAX&#41;](../DAX/hour-function-dax.md)  
[MINUTE Function &#40;DAX&#41;](../DAX/minute-function-dax.md)  
[YEAR Function &#40;DAX&#41;](../DAX/year-function-dax.md)  
[SECOND Function &#40;DAX&#41;](../DAX/second-function-dax.md)  
  
