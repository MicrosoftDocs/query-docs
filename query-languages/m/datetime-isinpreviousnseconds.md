---
title: "DateTime.IsInPreviousNSeconds | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e6e23e71-bc52-4186-882b-cbb801206949
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInPreviousNSeconds
DateTime.IsInPreviousNSeconds(dateTime as any, seconds as number) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the previous number of seconds, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|seconds: The number of seconds.|  
  
### Example 1  
Determine if the second before the current system time is in the previous two seconds.  
  
```  
DateTime.IsInPreviousNSeconds(DateTime.FixedLocalNow() - #duration(0,0,0,2), 2)  
```  
  
```  
Equals: true  
```  
