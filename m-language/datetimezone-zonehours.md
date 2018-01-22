---
title: "DateTimeZone.ZoneHours | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dbbb37b5-dd69-42b3-a10b-538eb5829a27
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.ZoneHours

  
## About  
Returns a time zone hour value from a DateTime value.  
  
```  
DateTimeZone.ZoneHours(dateTime as datetimezone) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to check against.|  
  
## Example  
  
```  
DateTimeZone.ZoneHours(DateTime.FromText("12:56:20-08:00")) equals -8  
```  
