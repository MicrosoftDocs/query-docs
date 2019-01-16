---
title: "Duration.ToText | Microsoft Docs"
ms.date: 1/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.ToText

## Syntax

<pre>
Duration.ToText(<b>duration</b> as nullable duration, optional <b>format</b> as nullable text) as nullable text
</pre>

## About

Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, <code>duration</code>. A text value that specifies the format can be provided as an optional second parameter, <code>format</code>. <ul> <li><code>duration</code>: A <code>duration</code> from which the textual representation is calculated.</li> <li><code>format</code>: <i>[Optional]</i> A <code>text</code> value that specifies the format.</li> </ul>

## Example 1

Convert `#duration(2, 5, 55, 20)` into a text value.

```powerquery-m
Duration.ToText(#duration(2, 5, 55, 20))
```

`
"2.05:55:20"
`

