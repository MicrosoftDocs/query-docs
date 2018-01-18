---
title: "EDATE Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.EDATE.f1"
helpviewer_keywords: 
  - "EDATE function"
ms.assetid: 5f78ec4f-8ee5-45cb-9853-fdb44147f5c1
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# EDATE Function (DAX)
Returns the date that is the indicated number of months before or after the start date. Use EDATE to calculate maturity dates or due dates that fall on the same day of the month as the date of issue.  
  
## Syntax  
  
```  
EDATE(<start_date>, <months>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**start_date**|A date in **datetime** or **text** format that represents the start date.|  
|**months**|An integer that represents the number of months before or after **start_date**.|  
  
## Return Value  
A date (**datetime**).  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates as sequential serial numbers, DAX works with dates in a **datetime** format. Dates stored in other formats are converted implicitly.  
  
If **start_date** is not a valid date, EDATE returns an error. Make sure that the column reference or date that you supply as the first argument is a date.  
  
If **months** is not an integer, it is truncated.  
  
When the date argument is a text representation of the date, the EDATE function uses the locale and date time settings of the client computer to understand the text value in order to perform the conversion. If the current date time settings represent a date in the format of Month/Day/Year, then the following string "1/8/2009" is interpreted as a datetime value equivalent to January 8th of 2009. However, if the current date time settings represent a date in the format of Day/Month/Year, the same string would be interpreted as a datetime value equivalent to August 1st of 2009.  
  
If the requested date is past the last day of the corresponding month, then the last day of the month is returned. For example, the following functions: EDATE("2009-01-29", 1), EDATE("2009-01-30", 1), EDATE("2009-01-31", 1) return February 28th of 2009; that corresponds to one month after the start date.  
  
This DAX function may return different results when used in a model that is deployed and then queried in DirectQuery mode. For more information about semantic differences in DirectQuery mode, see  [http://go.microsoft.com/fwlink/?LinkId=219171](http://go.microsoft.com/fwlink/?LinkId=219171).  
  
## Example  
The following example returns the date three months after the order date, which is stored in the column [TransactionDate].  
  
```  
=EDATE([TransactionDate],3)  
```  
  
## See Also  
[EOMONTH Function &#40;DAX&#41;](../DAX/eomonth-function-dax.md)  
[Date and Time Functions &#40;DAX&#41;](../DAX/date-and-time-functions-dax.md)  
  
