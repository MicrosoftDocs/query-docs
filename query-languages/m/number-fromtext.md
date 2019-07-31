---
title: "Number.FromText | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.FromText

## Syntax

<pre>
Number.FromText(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable number
</pre>
  
## About  
Returns a `number` value from the given text value, `text`. <ul> <li><code>text</code>: The textual representation of a number value. The representation must be in a common number format - "15", "3,423.10", "5.0E-10".</li> </ul>

## Example 1
Get the number value of `"4"`.

```powerquery-m
Number.FromText("4")
```

`4`

## Example 2
Get the number value of `"5.0e-10"`.

```powerquery-m
Number.FromText("5.0e-10")
```

`5E-10`
