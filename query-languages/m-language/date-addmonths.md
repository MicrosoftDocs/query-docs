---
title: "Date.AddMonths | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ca90ae1f-943d-44cc-82b7-a5abe72c6cfe
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.AddMonths

  
## About  
Returns a DateTime value with the month portion incremented by n months.  
  
```  
Date.AddMonths(dateTime as datetime, numberOfMonths as number) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add months to.|  
|numberOfMonths|The number of months to add.|  
  
## Remarks  
  
-   It also handles incrementing the year portion of the value as appropriate.  
  
## Examples  
  
```  
Date.AddMonths(DateTime.FromText("2011-02-19"), 5) equals 2011-07-19  
```  
  
```  
Date.AddMonths(DateTime.FromText("2010-12-01"), 2) equals 2011-02-01  
```  
