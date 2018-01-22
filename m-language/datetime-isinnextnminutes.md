---
title: "DateTime.IsInNextNMinutes | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e93fc934-a394-4a3f-994f-47b27330f4ee
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInNextNMinutes
DateTime.IsInNextNMinutes(dateTime as any, minutes as number) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next number of minutes, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|minutes: The number of minutes.|  
  
### Example 1  
Determine if the hour after the current system time is in the next two hours.  
  
```  
DateTime.IsInNextNHours(DateTime.LocalNow() + #duration(0,2,0,0), 2)  
```  
  
```  
Equals: true  
```  
