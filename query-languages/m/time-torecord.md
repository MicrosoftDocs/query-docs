---
title: "Time.ToRecord | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: eff03553-2158-4fda-b877-321d53ab10b4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Time.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
```  
Time.ToRecord(time as time) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|time|The time to parse.|  
  
## Example  
  
```  
Time.ToRecord(#time(12, 1, 2)) equals [Hour=12, Minute=1, Second=2]  
```  
