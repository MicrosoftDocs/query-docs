---
title: "TODAY function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TODAY

Returns the current date.  
  
## Syntax  
  
```dax
TODAY()  
```

## Return value

A date (**datetime**).  
  
## Remarks

- The TODAY function is useful when you need to have the current date displayed on a worksheet, regardless of when you open the workbook. It is also useful for calculating intervals.  
  
- If the TODAY function does not update the date when you expect it to, you might need to change the settings that control when the column or workbook is refreshed..  
  
- The NOW function is similar but returns the exact time, whereas TODAY returns the time value 12:00:00 PM for all dates.  
  
## Example

If you know that someone was born in 1963, you might use the following formula to find that person's age as of this year's birthday:  
  
```dax
= YEAR(TODAY())-1963  
```

This formula uses the TODAY function as an argument for the YEAR function to obtain the current year, and then subtracts 1963, returning the person's age.  
  
## See also

[Date and time functions](date-and-time-functions-dax.md)  
[NOW](now-function-dax.md)  
