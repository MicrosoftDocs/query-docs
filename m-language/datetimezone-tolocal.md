---
title: "DateTimeZone.ToLocal | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2d835f91-d6e3-4498-89eb-c2c29c766d0e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.ToLocal

  
## About  
Returns a DateTime value from the local time zone.  
  
```  
DateTimeZone.ToLocal(dateTime as datetimezone) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to convert.|  
  
## Example  
  
```  
//assuming local as PST   
dateTime  = DateTimeZone.FromText("2011-02-20T22:19:27+03:00")  
localTime=DateTimeZone.ToLocal(dateTime) equals 2011-02-20T11:19:27-08:00  
```  
