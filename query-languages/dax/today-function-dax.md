---
title: "TODAY Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TODAY Function (DAX)
Returns the current date.  
  
## Syntax  
  
```  
TODAY()  
```  
  
## Return Value  
A date (**datetime**).  
  
## Remarks  
The TODAY function is useful when you need to have the current date displayed on a worksheet, regardless of when you open the workbook. It is also useful for calculating intervals.  
  
> [!NOTE]  
> If the TODAY function does not update the date when you expect it to, you might need to change the settings that control when the column or workbook is refreshed..  
  
The NOW function is similar but returns the exact time, whereas TODAY returns the time value 12:00:00 PM for all dates.  
  
## Example  
If you know that someone was born in 1963, you might use the following formula to find that person's age as of this year's birthday:  
  
```  
=YEAR(TODAY())-1963  
```  
This formula uses the TODAY function as an argument for the YEAR function to obtain the current year, and then subtracts 1963, returning the person's age.  
  
## See Also  
[Date and Time Functions &#40;DAX&#41;](date-and-time-functions-dax.md)  
[NOW Function &#40;DAX&#41;](now-function-dax.md)  
  
