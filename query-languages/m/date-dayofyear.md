---
title: "Date.DayOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4548f4fd-2d47-4dc0-a700-422367b6259e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.DayOfYear

  
## About  
Returns a number that represents the day of the year from a DateTime value.  
  
```  
Date.DayOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Examples  
  
```  
Date.DayOfYear(DateTime.FromText("2011-03-01")) equals 60  
```  
  
```  
Date.DayOfYear(DateTime.FromText("2012-03-01")) equals 61  
```  
