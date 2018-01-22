---
title: "Date.StartOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c53b3c6a-216c-426d-bcfd-54389b9602b4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.StartOfYear

  
## About  
Returns a DateTime value representing the start of the year.  
  
```  
Date.StartOfYear(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the year.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```  
dateTime=DateTimeZone.FromText("2011-02-21T12:30:00-08:00")   
Date.StartOfYear(dateTime) equals 2011-01-01T00:00:00-08:00  
```  
