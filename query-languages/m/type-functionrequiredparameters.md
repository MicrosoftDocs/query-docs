---
title: "Type.FunctionRequiredParameters | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.FunctionRequiredParameters

## Syntax

<pre>
Type.FunctionRequiredParameters(<b>type</b> as type) as number  
</pre>
  
## About  
Returns a number indicating the minimum number of parameters required to invoke the input `type` of function.

## Example 1
Find the number of required parameters to the function `(x as number, optional y as text)`.

```powerquery-m
Type.FunctionRequiredParameters(type function (x as number, optional y as text) as any)
```

`1`
