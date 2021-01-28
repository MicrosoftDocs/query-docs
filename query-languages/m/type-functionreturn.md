---
description: "Learn more about: Type.FunctionReturn"
title: "Type.FunctionReturn | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.FunctionReturn

## Syntax

<pre>
Type.FunctionReturn(<b>type</b> as type) as type  
</pre>
  
## About  
Returns a type returned by a function `type`.

## Example 1
Find the return type of `() as any)`.

```powerquery-m
Type.FunctionReturn(type function () as any)
```

`type any`
