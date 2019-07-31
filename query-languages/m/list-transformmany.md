---
title: "List.TransformMany | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.TransformMany

## Syntax

<pre>
List.TransformMany(<b>list</b> as list, <b>collectionTransform</b> as function, <b>resultTransform</b> as function) as list
</pre>
  
## About  
Returns a list whose elements are projected from the input list. The `collectionTransform` function is applied to each element, and the `resultTransform` function is invoked to construct the resulting list. The `collectionSelector` has the signature (x as Any) => ... where x is an element in list. The `resultTransform` projects the shape of the result and has the signature (x as Any, y as Any) => ... where x is the element in list and y is the element obtained by applying the `collectionTransform` to that element.
