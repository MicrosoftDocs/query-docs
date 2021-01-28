---
description: "Learn more about: Text.Combine"
title: "Text.Combine | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Combine

## Syntax

<pre>
Text.Combine(<b>texts</b> as list, optional <b>separator</b> as nullable text) as text
</pre>
  
## About  
Returns the result of combining the list of text values, `texts`, into a single text value. An optional separator used in the final combined text may be specified, `separator`.

## Example 1
Combine text values "Seattle" and "WA".

```powerquery-m
Text.Combine({"Seattle", "WA"})
```

`"SeattleWA"`

## Example 2
Combine text values "Seattle" and "WA" separated by a comma and a space, ", ".

```powerquery-m
Text.Combine({"Seattle", "WA"}, ", ")
```

`"Seattle, WA"`
