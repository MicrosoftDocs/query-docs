---
title: "DateTime.IsInNextSecond | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5ac310a9-a193-4bc2-b198-0ff11daad744
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.IsInNextSecond
DateTime.IsInNextSecond(dateTime as any) as nullable logical  
  
## About  
Indicates whether the given datetime value occurs during the next second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the second after the current system time is in the next second.  
  
```  
DateTime.IsInNextSecond(DateTime.FixedLocalNow() + #duration(0,0,0,1))  
```  
  
```  
Equals: true  
```  
