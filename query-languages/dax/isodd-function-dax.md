---
title: "ISODD Function (DAX) | Microsoft Docs"
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
ms.assetid: d7d64e90-002d-40e0-8bf2-bac4921d2736
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# ISODD Function (DAX)
Returns TRUE if number is odd, or FALSE if number is even.  
  
## Syntax  
  
```  
ISODD(number)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return Value  
Returns TRUE if number is odd, or FALSE if number is even.  
  
## Remarks  
If number is nonnumeric, ISODD returns the #VALUE! error value.  
  
