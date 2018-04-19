---
title: "List.MatchesAny | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
