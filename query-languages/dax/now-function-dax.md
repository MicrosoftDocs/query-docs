---
title: "NOW Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NOW Function (DAX)
Returns the current date and time in **datetime** format.  
  
The NOW function is useful when you need to display the current date and time on a worksheet or calculate a value based on the current date and time, and have that value updated each time you open the worksheet.  
  
## Syntax  
  
```  
NOW()  
```  
  
## Return Value  
A date (**datetime)**.  
  
## Remarks  

The result of the NOW function changes only when the column that contains the formula is refreshed. It is not updated continuously.  
  
The TODAY function returns the same date but is not precise with regard to time; the time returned is always 12:00:00 AM and only the date is updated.  
  
## Example  
The following example returns the current date and time plus 3.5 days:  
  
```  
=NOW()+3.5  
```  
  
## See Also  
[UTCNOW Function](utcnow-function-dax.md)   
[TODAY Function &#40;DAX&#41;](today-function-dax.md)  
  
