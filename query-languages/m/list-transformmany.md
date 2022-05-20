---
description: "Learn more about: List.TransformMany"
title: "List.TransformMany | Microsoft Docs"
ms.date: 10/18/2021
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.TransformMany

## Syntax

<pre>
List.TransformMany(<b>list</b> as list, <b>collectionTransform</b> as function, <b>resultTransform</b> as function) as list
</pre>
  
## About  

Returns a list whose elements are projected from the input list. The `collectionTransform` function is applied to each element, and the `resultTransform` function is invoked to construct the resulting list. The `collectionTransform` has the signature `(x as any) as list => ...` where `x` is an element in `list`. The `resultTransform` projects the shape of the result and has the signature `(x as any, y as any) as any => ...` where `x` is the element in `list` and `y` is the element obtained by applying the `collectionTransform` to that element.
