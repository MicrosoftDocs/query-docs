---
description: "Learn more about: Type.FunctionParameters"
title: "Type.FunctionParameters | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Type.FunctionParameters

## Syntax

<pre>
Type.FunctionParameters(<b>type</b> as type) as record
</pre>
  
## About

Returns a record with field values set to the name of the parameters of `type`, and their values set to their corresponding types.

## Example 1

Find the types of the parameters to the function `(x as number, y as text)`.

**Usage**

```powerquery-m
Type.FunctionParameters(type function (x as number, y as text) as any)
```

**Output**

`[x = type number, y = type text]`
