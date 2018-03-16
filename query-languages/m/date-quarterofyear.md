---
title: "Date.QuarterOfYear | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 344550f7-7a72-4ca0-9c94-fc12dbb14dc6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.QuarterOfYear

  
## About  
Returns a number between 1 and 4 for the quarter of the year from a DateTime value.  
  
```  
Date.QuarterOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Examples  
  
```  
Date.QuarterOfYear(DateTime.FromText("2011-03-21")) equals 1  
```  
  
```  
Date.QuarterOfYear(DateTime.FromText("2011-11-21")) equals 4  
```  
