---
title: "Character.FromNumber | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Character.FromNumber

## Syntax

<pre>  
Character.FromNumber(<b>number</b> as nullable number) as nullable text 
</pre> 
  
## About  
Returns the character equivalent of the number.

## Example 1
Given the number 9, find the character value.

```powerquery-m
Character.FromNumber(9)
```

`"#(tab)"`
