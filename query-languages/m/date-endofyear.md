---
title: "Date.EndOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a883d7ac-18d0-4be9-8343-98324d4339fb
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.EndOfYear

  
## About  
Returns a DateTime value for the end of the year.  
  
```  
Date.EndOfYear(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the year.  
  
-   The timezone information is persisted.  
  
## Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.EndOfYear(dateTime) equals 2011-12-31T23:59:59-08:00  
```  
