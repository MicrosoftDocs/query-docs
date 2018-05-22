---
title: "MINUTE Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MINUTE Function (DAX)
Returns the minute as a number from 0 to 59, given a date and time value.  
  
## Syntax  
  
```  
MINUTE(<datetime>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**datetime**|A **datetime** value or text in an accepted time format, such as 16:48:00 or 4:48 PM.|  
  
## Return Value  
An integer number from 0 to 59.  
  
## Remarks  
In contrast to Microsoft Excel, which stores dates and times in a serial numeric format, DAX uses a **datetime** data type for dates and times. You can provide the **datetime** value to the MINUTE function by referencing a column that stores dates and times, by using a date/time function, or by using an expression that returns a date and time.  
  
When the **datetime** argument is a text representation of the date and time, the function uses the locale and date/time settings of the client computer to understand the text value in order to perform the conversion. Most locales use the colon (:) as the time separator and any input text using colons as time separators will parse correctly. Verify your locale settings to understand your results.  
  
## Example  
The following example returns the minute from the value stored in the **TransactionTime** column of the **Orders** table.  
  
```  
=MINUTE(Orders[TransactionTime])  
```  
  
## Example  
The following example returns 45, which is the number of minutes in the time 1:45 PM.  
  
```  
=MINUTE("March 23, 2008 1:45 PM")  
```  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[HOUR Function &#40;DAX&#41;](hour-function-dax.md)  
[YEAR Function &#40;DAX&#41;](year-function-dax.md)  
[SECOND Function &#40;DAX&#41;](second-function-dax.md)  
  
