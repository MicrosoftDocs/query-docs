---
title: "Date.AddDays | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0a533a57-c9ad-42f3-9bcb-f37f0870d91f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.AddDays

  
## About  
Returns a Date/DateTime/DateTimeZone value with the day portion incremented by the number of days provided. It also handles incrementing the month and year potions of the value as appropriate.  
  
```  
Date.AddDays(dateTime, days as number)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add days to.|  
|days|The number of days to add.|  
  
## Examples  
  
```  
Date.AddDays(DateTime.FromText("2011-02-19"), 5) equals 2011-02-24  
```  
  
```  
Date.AddDays(DateTime.FromText("2011-02-19"), -2) equals 2011-02-17  
```  
  
```  
Date.AddDays(DateTime.FromText("2011-12-31"), 1) equals 2012-01-01  
```  
