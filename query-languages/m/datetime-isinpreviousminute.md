---
title: "DateTime.IsInPreviousMinute | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 82e7904b-6fa6-4e9b-a5f1-be437ebf3229
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInPreviousMinute
DateTime.IsInPreviousMinute(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the previous minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the minute before the current system time is in the previous minute.  
  
```  
DateTime.IsInPreviousMinute(DateTime.LocalNow() - #duration(0,0,1,0))  
```  
  
```  
Equals: true  
```  
