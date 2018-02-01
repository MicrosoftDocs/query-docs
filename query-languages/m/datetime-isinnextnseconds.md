---
title: "DateTime.IsInNextNSeconds | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cd207407-7b43-428a-9bdc-964af97f5cd4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInNextNSeconds
DateTime.IsInNextNSeconds(dateTime as any, seconds as number) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next number of seconds, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|seconds: The number of seconds.|  
  
### Example 1  
Determine if the second after the current system time is in the next two seconds.  
  
```  
DateTime.IsInNextNSeconds(DateTime.FixedLocalNow() + #duration(0,0,0,2), 2)  
```  
  
```  
Equals: true  
```  
