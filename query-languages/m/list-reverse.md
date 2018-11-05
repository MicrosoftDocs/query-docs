---
title: "List.Reverse | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Reverse

  
## About  
Returns a list that reverses the items in a list.  
  
## Syntax

<pre>
List.Reverse(list as list) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.Reverse({1, 2, 3, 4, 5}) equals {5, 4, 3, 2, 1}  
```  
