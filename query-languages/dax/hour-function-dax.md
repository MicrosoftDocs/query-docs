---
title: "HOUR Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.HOUR.f1"
helpviewer_keywords: 
  - "HOUR function"
ms.assetid: a78dbb05-1a96-4a7c-b414-8e3973d47f01
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# HOUR Function (DAX)
Returns the hour as a number from 0 (12:00 A.M.) to 23 (11:00 P.M.).  
  
## Syntax  
  
```  
HOUR(<datetime>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**datetime**|A **datetime** value, such as 16:48:00 or 4:48 PM.|  
  
## Return Value  
An integer number from 0 to 23.  
  
## Remarks  
The HOUR function takes as argument the time that contains the hour you want to find. You can supply the time by using a date/time function, an expression that returns a **datetime**, or by typing the value directly in one of the accepted time formats. Times can also be entered as any accepted text representation of a time.  
  
When the **datetime** argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any input text using colons as time separators will parse correctly. Review your locale settings to understand your results.  
  
## Example  
The following example returns the hour from the **TransactionTime** column of a table named **Orders**.  
  
```  
=HOUR('Orders'[TransactionTime])  
```  
  
## Example  
The following example returns 15, meaning the hour corresponding to 3 PM in a 24-hour clock. The text value is automatically parsed and converted to a date/time value.  
  
```  
=HOUR("March 3, 2008 3:00 PM")  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[MINUTE Function &#40;DAX&#41;](minute-function-dax.md)  
[YEAR Function &#40;DAX&#41;](year-function-dax.md)  
[SECOND Function &#40;DAX&#41;](second-function-dax.md)  
  
