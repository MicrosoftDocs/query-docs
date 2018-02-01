---
title: "Date.AddWeeks | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d271c85b-18bc-43d1-998a-9272d1c29a0d
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.AddWeeks

  
## About  
Returns a Date/DateTime/DateTimeZone value incremented by the number of weeks provided. Each week is defined as a duration of seven days. It also handles incrementing the month and year potions of the value as appropriate.  
  
```  
Date.AddWeeks(dateTime, weeks as number)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add weeks to.|  
|weeks|The number of weeks to add.|  
  
## Examples  
  
```  
Date.AddWeeks(DateTime.FromText("2011-02-19"), 1) equals 2011-02-26  
```  
  
```  
Date.AddWeeks(DateTime.FromText("2011-02-19"), -2) equals 2011-02-05  
```  
  
```  
Date.AddWeeks(DateTime.FromText("2011-12-31"), 1) equals 2012-01-07  
```  
