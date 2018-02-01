---
title: "Date.StartOfDay | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ebb58e60-4cc8-46fc-8cdf-b7e00026dd04
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.StartOfDay

  
## About  
Returns a DateTime value for the start of the day.  
  
```  
Date.StartOfDay(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the day.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.StartOfDay(dateTime) equals 2011-02-21T00:00:00-08:00  
```  
