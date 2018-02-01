---
title: "Date.Year | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 901b5b17-f1ef-4c72-86b0-2b073484cbf5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.Year

  
## About  
Returns the year from a DateTime value.  
  
```  
Date.Year(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the year for.|  
  
## Example  
  
```  
Date.Year(DateTime.FromText("2011-02-19")) equals 2011  
```  
