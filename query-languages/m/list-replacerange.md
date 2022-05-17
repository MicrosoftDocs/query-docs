---
description: "Learn more about: List.ReplaceRange"
title: "List.ReplaceRange | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.ReplaceRange

## Syntax

<pre>
List.ReplaceRange(<b>list</b> as list, <b>index</b> as number, <b>count</b> as number, <b>replaceWith</b> as list) as list
</pre>
  
## About

Replaces `count` values in the `list` with the list `replaceWith`, starting at specified position, `index`.

## Example 1

Replace {7, 8, 9} in the list {1, 2, 7, 8, 9, 5} with {3, 4}.

**Usage**

```powerquery-m
List.ReplaceRange({1, 2, 7, 8, 9, 5}, 2, 3, {3, 4})
```

**Output**

`{1, 2, 3, 4, 5}`
