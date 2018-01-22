---
title: "Date.Day | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1012919c-96aa-493e-84c7-be32792d9da9
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.Day

  
## About  
Returns the day for a DateTime value.  
  
```  
Date.Day(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the day for.|  
  
## Example  
  
```  
Date.Day(DateTime.FromText("2011-02-19")) equals 19  
```  
