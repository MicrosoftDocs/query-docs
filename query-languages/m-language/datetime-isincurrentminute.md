---
title: "DateTime.IsInCurrentMinute | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cd24488d-762a-49ca-9026-33fef7da642c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInCurrentMinute
DateTime.IsInCurrentMinute(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the current minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the current system time is in the current minute.  
  
```  
DateTime.IsInCurrentMinute(DateTime.LocalNow())  
```  
  
```  
Equals: true  
```  
