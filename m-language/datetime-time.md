---
title: "DateTime.Time | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 837eea87-001d-4b16-b681-15e2d300fa5a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.Time

  
## About  
Returns a time part from a DateTime value.  
  
```  
DateTime.Time(dateTime as datetime) as nullable time  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The **DateTime** to parse.|  
  
## Example  
  
```  
DateTime.Time(#datetime(2010, 5, 4, 6, 5, 4)) equals #time(6, 5, 4)  
```  
