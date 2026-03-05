---
description: "Learn more about: Type.FunctionRequiredParameters"
title: "Type.FunctionRequiredParameters"
ms.subservice: m-source
ms.topic: reference
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

**Usage**

```powerquery-m
Type.FunctionRequiredParameters(type function (x as number, optional y as text) as any)
```

**Output**

`1`
