---
title: "DateTime.AddZone | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9db50fd4-3208-4791-98d0-6cf13f2f710c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTime.AddZone

  
## About  
Adds the timezonehours as an offset to the input datetime value and returns a new datetimezone value.  
  
```  
DateTime.AddZone(dateTime as nullable datetime, timezoneHours as number, optional timezoneMinutes as nullable number) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|A DateTime to modify.|  
|timezoneHours|The hours to add.|  
|optional timezoneMinutes|The minuts to add.|  
  
## Example  
  
```  
DateTime.AddZone(#datetime(2010, 5, 4, 6, 5, 5), 8) equals #datetimezone(2010, 5, 4, 6, 5, 5, 8, 0)  
```  
