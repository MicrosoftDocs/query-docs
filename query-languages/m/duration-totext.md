---
title: "Duration.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 384e2bc3-b15e-4c36-bfec-72d36e054d63
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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

