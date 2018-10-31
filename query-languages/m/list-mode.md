---
title: "List.Mode | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Mode

  
## About  
Returns an item that appears most commonly in a list.  
  
## Syntax

<pre>
List.Mode(list as list, optional equationCriteria as any)as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Controls the sort order. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789380"></a>Remarks  
  
-   If more than 1 item appears with the same maximum frequency, the last item in the first appearance order is chosen.  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.Mode({"A", 1, 4, 5, 2, "B", 3, 5, 5, 4, 4}) equals 5  
```  
