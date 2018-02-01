---
title: "Time.StartOfHour | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e0a5e778-dea1-407a-888a-3b838ca4d5a7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Time.StartOfHour

  
## About  
Returns the first value of the hour from a time value.  
  
```  
Time.StartOfHour(datetime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Time.StartOfHour(#datetime(2013, 4, 5, 1, 3, 45)) equals #datetime(2013, 4, 5, 1, 0, 0)  
```  
