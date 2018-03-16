---
title: "DateTime.IsInCurrentSecond | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2c267ba6-8966-4f1a-86f7-71c337b11f32
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInCurrentSecond
DateTime.IsInCurrentSecond(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the current second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the current system time is in the current second.  
  
```  
DateTime.IsInCurrentSecond(DateTime.FixedLocalNow())  
```  
  
```  
Equals: true  
```  
