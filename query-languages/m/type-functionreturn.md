---
description: "Learn more about: Type.FunctionReturn"
title: "Type.FunctionReturn"
ms.subservice: m-source
ms.topic: reference
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

**Usage**

```powerquery-m
Type.FunctionReturn(type function () as any)
```

**Output**

`type any`
