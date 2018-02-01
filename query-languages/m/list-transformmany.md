---
title: "List.TransformMany | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 85e0d325-45f8-4bfc-a541-8a95dc6cb8e8
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.TransformMany

  
## About  
Returns a list whose elements are projected from the input list.  
  
```  
List.TransformMany(list as list, collectionTransform as Function, resultTransform as Function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|collectionTransform|The collectionTransform function is applied to each element, and the resultTransform function is invoked to construct the resulting list. The collectionSelector has the signature (x as any) =&gt; … where x is an element in list.|  
|resultTransform|The resultTransform projects the shape of the result and has the signature (x as any, y as any) =&gt; … where x is the element in list and y is the element obtained by applying the collectionTransform to that element.|  
  
## Example  
  
```  
List.TransformMany({1, 2}, (value) => {value + 1}, (oldValue, newValue) => oldValue * newValue) equals { 2, 6 }  
```  
