---
title: "Duration.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.ToText
<code>Duration.ToText(**duration** as nullable duration, optional **format** as nullable text) as nullable text</code>

## About
Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, <code>duration</code>. A text value that specifies the format can be provided as an optional second parameter, <code>format</code>. 

-    <code>duration</code>: A <code>duration</code> from which the textual representation is calculated.
-    <code>format</code>: [Optional] A <code>text</code> value that specifies the format.

## Example 1

Convert <code>#duration(2, 5, 55, 20)</code> into a text value.

```
Duration.ToText(#duration(2, 5, 55, 20))
```


```
"2.05:55:20"
```

