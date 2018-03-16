---
title: "List.MatchesAll | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d4223e95-586a-45f8-8af8-05581f8666da
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.MatchesAll

  
## About  
Returns true if all items in a list meet a condition.  
  
```  
List.MatchesAll(list as list, condition as Function) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to qualify against.|  
  
## Examples  
  
```  
List.MatchesAll({2, 4, 6}, each Number.Mod(_,2) = 0) equals true  
```  
  
```  
List.MatchesAll({2, 4, 5}, each Number.Mod(_,2) = 0) equals false  
```  
