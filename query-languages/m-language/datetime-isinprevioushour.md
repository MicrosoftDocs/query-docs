---
title: "DateTime.IsInPreviousHour | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e0896666-5fd0-401b-b6ae-78ae85311142
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInPreviousHour
DateTime.IsInPreviousHour(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the previous hour, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the hour before the current system time is in the previous hour.  
  
```  
DateTime.IsInPreviousHour(DateTime.LocalNow() - #duration(0,1,0,0))  
```  
  
```  
Equals: true  
```  
