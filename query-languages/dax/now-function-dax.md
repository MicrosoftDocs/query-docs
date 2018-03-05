---
title: "NOW Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.NOW.f1"
helpviewer_keywords: 
  - "NOW function"
ms.assetid: d4ee25ed-3066-42c2-a792-87604644de9a
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
