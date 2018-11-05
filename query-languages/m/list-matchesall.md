---
title: "List.MatchesAll | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.MatchesAll

  
## About  
Returns true if all items in a list meet a condition.  
  
## Syntax

<pre>
List.MatchesAll(list as list, condition as Function) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to qualify against.|  
  
## Examples  
  
```powerquery-m
List.MatchesAll({2, 4, 6}, each Number.Mod(_,2) = 0) equals true  
```  
  
```powerquery-m
List.MatchesAll({2, 4, 5}, each Number.Mod(_,2) = 0) equals false  
```  
