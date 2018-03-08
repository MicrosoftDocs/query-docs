---
title: "DateTime.IsInNextMinute | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a0eaa743-fbe2-41c1-80fb-4fb4cd1808eb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInNextMinute
DateTime.IsInNextMinute(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the minute after the current system time is in the next minute.  
  
```  
DateTime.IsInNextMinute(DateTime.LocalNow() + #duration(0,0,1,0))  
```  
  
```  
Equals: true  
```  
