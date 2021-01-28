---
description: "Learn more about: Duration.ToText"
title: "Duration.ToText | Microsoft Docs"
ms.date: 06/08/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.ToText

## Syntax

<pre>
Duration.ToText(<b>duration</b> as nullable duration, optional <b>format</b> as nullable text) as nullable text
</pre>

## About

Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, `duration`.

* `duration`: A `duration` from which the textual representation is calculated.
* `format`: *[Optional]* Deprecated, will throw an error if not null.

## Example 1

Convert `#duration(2, 5, 55, 20)` into a text value.

```powerquery-m
Duration.ToText(#duration(2, 5, 55, 20))
```

`
"2.05:55:20"
`

