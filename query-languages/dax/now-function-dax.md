---
title: "NOW function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NOW

Returns the current date and time in **datetime** format.  
  
The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.  
  
## Syntax  
  
```dax
NOW()  
```
  
## Return value

A date (**datetime)**.  
  
## Remarks  

- The result of the NOW function changes only when the column that contains the formula is refreshed. It is not updated continuously.  

- In the Power BI Service, the result of the NOW function is always in the UTC timezone.

- The TODAY function returns the same date but is not precise with regard to time; the time returned is always 12:00:00 AM and only the date is updated.  
  
## Example

The following example returns the current date and time plus 3.5 days:  
  
```dax
= NOW()+3.5  
```
  
## See also

[UTCNOW function](utcnow-function-dax.md)  
[TODAY function](today-function-dax.md)  
