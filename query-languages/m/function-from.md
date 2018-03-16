---
title: "Function.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c4880cdc-4e36-4f6b-92d2-8ea026d1ce37
caps.latest.revision: 3
author: "MarkMcGeeAtAquent"
ms.author: "v-mamcge"
manager: "kfile"
---
# Function.From
<code>Function.From(<b>functionType</b> as type, <b>function</b> as function) as function</code>

## About
Takes a unary function `function` and creates a new function with the type `functionType` that constructs a list out of its arguments and passes it to `function`.

## Example 1
Converts List.Sum into a two-argument function whose arguments are added together.

```
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

`3`

## Example 2
Converts a function taking a list into a two-argument function.

```
Function.From(type function (a as text, b as text) as text, (list) => list{0} & list{1})("2", "1")
```

`"21"`

