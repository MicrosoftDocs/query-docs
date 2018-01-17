---
title: "Date.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3b063df3-584c-4c94-9a15-0e2eb471c7dc
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.ToText
<code>Date.ToText(**date** as nullable date, optional **format** as nullable text, optional **culture** as nullable text) as nullable text</code>

## About
Returns a textual representation of <code>date</code>, the Date value, <code>date</code>. This function takes in an optional format parameter <code>format</code>. For a complete list of supported formats, please refer to the Library specification document.

## Example 1
Get a textual representation of #date(2010, 12, 31).

```
Date.ToText(#date(2010, 12, 31))
```

```
"12/31/2010"
```


## Example 2
Get a textual representation of #date(2010, 12, 31) with format option.

```
Date.ToText(#date(2010, 12, 31), "yyyy/MM/dd")
```

```
"2010/12/31"
```







