---
title: "Date.AddYears | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a1c42f09-9521-497f-97f1-65dabd02ee2a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.AddYears

  
## About  
Returns a DateTime value with the year portion incremented by n years.  
  
```  
Date.AddYears(dateTime as datetime, years as number) as datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add years to.|  
|years|The number of years to add.|  
  
## Example  
  
```  
Date.AddYears(DateTime.FromText("2011-02-19"), 10) equals 2021-02-19  
```  
