---
title: "List.TransformMany | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.TransformMany

  
## About  
Returns a list whose elements are projected from the input list.  
  
## Syntax

<pre>
List.TransformMany(list as list, collectionTransform as Function, resultTransform as Function) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|collectionTransform|The collectionTransform function is applied to each element, and the resultTransform function is invoked to construct the resulting list. The collectionSelector has the signature (x as any) =&gt; … where x is an element in list.|  
|resultTransform|The resultTransform projects the shape of the result and has the signature (x as any, y as any) =&gt; … where x is the element in list and y is the element obtained by applying the collectionTransform to that element.|  
  
## Example  
  
```powerquery-m
List.TransformMany({1, 2}, (value) => {value + 1}, (oldValue, newValue) => oldValue * newValue) equals { 2, 6 }  
```  
