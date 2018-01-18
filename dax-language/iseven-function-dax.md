---
title: "ISEVEN Function (DAX) | Microsoft Docs"
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
ms.assetid: 4f76840c-f014-4887-9c43-6ad87f697c23
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ISEVEN Function (DAX)
Returns TRUE if number is even, or FALSE if number is odd.  
  
## Syntax  
  
```  
ISEVEN(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return Value  
Returns TRUE if number is even, or FALSE if number is odd.  
  
## Remarks  
If number is nonnumeric, ISEVEN returns the #VALUE! error value.  
  
