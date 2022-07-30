---
description: "Learn more about: Duration.ToText"
title: "Duration.ToText | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Duration.ToText(#duration(2, 5, 55, 20))
```

**Output**

`"2.05:55:20"`
