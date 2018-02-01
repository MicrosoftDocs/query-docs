---
title: "RANDBETWEEN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.RANDBETWEEN.f1"
helpviewer_keywords: 
  - "RANDBETWEEN function"
ms.assetid: 7ef4d08e-796b-41c4-a124-ad97da50e9a2
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# RANDBETWEEN Function (DAX)
Returns a random number in the range between two numbers you specify.  
  
## Syntax  
  
```  
RANDBETWEEN(<bottom>,<top>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Bottom**|The smallest integer the function will return.|  
|**Top**|The largest integer the function will return.|  
  
## Return Value  
A whole number.  
  
## Remarks  
This DAX function is not supported for use in DirectQuery mode. For more information about limitations in DirectQuery models, see  [http://go.microsoft.com/fwlink/?LinkId=219172](http://go.microsoft.com/fwlink/?LinkId=219172).  
  
## Example  
The following formula returns a random number between 1 and 10.  
  
```  
=RANDBETWEEN(1,10)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
