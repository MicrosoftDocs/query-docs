---
title: "List.MatchesAny | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6b47b5aa-d570-41dd-a0ee-5853df86d325
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.MatchesAny

  
## About  
Returns true if any item in a list meets a condition.  
  
```  
List.MatchesAny(list as list, condition as Function) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to qualify against.|  
  
## Examples  
  
```  
List.MatchesAny({2, 4, 6}, each Number.Mod(_, 2) = 0) equals true  
```  
  
```  
List.MatchesAny({1, 3, 5}, each Number.Mod(_, 2) = 0) equals false  
```  
