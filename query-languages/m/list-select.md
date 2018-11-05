---
title: "List.Select | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Select

  
## About  
Selects the items that match a condition.  
  
## Syntax

<pre>
List.Select(list as list, condition as function) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to match against.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.Select({1, 3, 5}, each _ > 2) equals {3 ,5}  
```  
