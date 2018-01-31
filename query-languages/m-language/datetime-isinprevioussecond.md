---
title: "DateTime.IsInPreviousSecond | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 24c98494-4f3c-4e75-bae0-a523e8361c13
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInPreviousSecond
DateTime.IsInPreviousSecond(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the previous second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the second before the current system time is in the previous second.  
  
```  
DateTime.IsInPreviousSecond(DateTime.FixedLocalNow() - #duration(0,0,0,1))  
```  
  
```  
Equals: true  
```  
