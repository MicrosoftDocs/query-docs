---
title: "Date.EndOfMonth | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5f8c30ab-f99d-4297-8bf3-9ad926da5e37
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.EndOfMonth

  
## About  
Returns a DateTime value for the end of the month.  
  
```  
Date.EndOfMonth(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the month.  
  
-   The timezone information is persisted.  
  
## Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.EndOfMonth(dateTime) equals 2011-02-28T23:59:59-08:00  
```  
