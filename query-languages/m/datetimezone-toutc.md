---
title: "DateTimeZone.ToUtc | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6981c416-a584-49a8-b2e3-c5b287bb9287
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.ToUtc

  
## About  
Returns a DateTime value to the Utc time zone.  
  
```  
DateTimeZone.ToUtc(dateTime as datetimezone) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to convert.|  
  
## Example  
  
```  
dateTime  = DateTimeZone.FromText("2011-02-20T22:19:27+03:00")  
```  
  
```  
utcTime = DateTimeZone.ToUtc(dateTime)equals 2011-02-20T19:19:27+00:00  
```  
