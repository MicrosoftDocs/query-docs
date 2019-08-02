---
title: "Type.ListItem | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.ListItem

## Syntax

<pre>
Type.ListItem(<b>type</b> as type) as type 
</pre>
  
## About  
Returns an item type from a list `type`.

## Example 1
Find item type from the list `{number}`.

```powerquery-m
Type.ListItem(type {number})
```

`type number`
