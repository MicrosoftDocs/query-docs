---
title: "Logical.ToText | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.ToText

## Syntax

<pre>
Logical.ToText(<b>logicalValue</b> as nullable logical) as nullable text  
</pre>
  
## About  
Creates a text value from the logical value `logicalValue`, either `true` or `false`. If `logicalValue` is not a logical value, an exception is thrown.

## Example 1
Create a text value from the logical `true`.

```powerquery-m
Logical.ToText(true)
```

`"true"`
