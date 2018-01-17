---
title: "YEARFRAC Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.YEARFRAC.f1"
helpviewer_keywords: 
  - "YEARFRAC function"
ms.assetid: 52f6cba8-1a4b-4430-8049-77df5a018cdd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# YEARFRAC Function (DAX)
Calculates the fraction of the year represented by the number of whole days between two dates. Use the YEARFRAC worksheet function to identify the proportion of a whole year's benefits or obligations to assign to a specific term.  
  
## Syntax  
  
```  
YEARFRAC(<start_date>, <end_date>, <basis>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**start_date**|The start date in **datetime** format.|  
|**end_date**|The end date in **datetime** format.|  
|**basis**|(Optional) The type of day count basis to use. All arguments are truncated to integers.<br /><br />Basis - Description<br /><br />0 - US (NASD) 30/360<br /><br />1 -  Actual/actual<br /><br />2 - Actual/360<br /><br />3 -   Actual/365<br /><br />4 - European 30/360|  
  
## Return Value  
A decimal number. The internal data type is a signed IEEE 64-bit (8-byte) double-precision floating-point number.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as serial numbers, DAX uses a **datetime** format to work with dates and times. If you need to view dates as serial numbers, you can use the formatting options in Excel.  
  
If **start_date** or **end_date** are not valid dates, YEARFRAC returns an error.  
  
If **basis** &lt; 0 or if **basis** &gt; 4, YEARFRAC returns an error.  
  
## Example  
The following example returns the fraction of a year represented by the difference between the dates in the two columns, `TransactionDate` and `ShippingDate`:  
  
```  
=YEARFRAC(Orders[TransactionDate],Orders[ShippingDate])  
```  
  
## Example  
The following example returns the fraction of a year represented by the difference between the dates, January 1 and March 1:  
  
```  
=YEARFRAC("Jan 1 2007","Mar 1 2007")  
```  
Use four-digit years whenever possible, to avoid getting unexpected results. When the year is truncated, the current year is assumed. When the date is or omitted, the first date of the month is assumed.  
  
The second argument, **basis**, has also been omitted. Therefore, the year fraction is calculated according to the US (NASD) 30/360 standard.  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
[WEEKNUM Function &#40;DAX&#41;](../DAX/weeknum-function-dax.md)  
[YEARFRAC Function &#40;DAX&#41;](../DAX/yearfrac-function-dax.md)  
[WEEKDAY Function &#40;DAX&#41;](../DAX/weekday-function-dax.md)  
  
