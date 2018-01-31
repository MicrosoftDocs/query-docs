---
title: "Date.StartOfMonth | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 5a7b338e-3492-48f2-802c-874db8574ed5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.StartOfMonth

  
## About  
Returns a DateTime value representing the start of the month.  
  
```  
Date.StartOfMonth(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the month.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");  
Date.StartOfMonth(dateTime) equals 2011-02-01T00:00:00-08:00  
```  
