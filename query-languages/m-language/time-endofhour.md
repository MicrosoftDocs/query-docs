---
title: "Time.EndOfHour | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1c75b7d9-a238-4bb9-bd98-f5b7edac6d3d
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Time.EndOfHour

  
## About  
Returns a DateTime value from the end of the hour.  
  
```  
Time.EndOfHour(dateTime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The time portion is reset to its terminating values for the hour.  
  
-   The timezone information is persisted.  
  
## Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Time.EndOfHour(dateTime) equals 2011-02-21T12:59:59-08:00  
```  
