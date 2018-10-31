---
title: "Duration.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.ToText
`Duration.ToText(**duration** as nullable duration, optional **format** as nullable text) as nullable text`

## About
Returns a textual representation in the form "day.hour:mins:sec" of the given duration value, `duration`. A text value that specifies the format can be provided as an optional second parameter, `format`. 

-    `duration`: A `duration` from which the textual representation is calculated.
-    `format`: [Optional] A `text` value that specifies the format.

## Example 1

Convert `#duration(2, 5, 55, 20)` into a text value.

```
Duration.ToText(#duration(2, 5, 55, 20))
```


```
"2.05:55:20"
```

