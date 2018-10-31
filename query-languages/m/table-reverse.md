---
title: "Table.Reverse | Microsoft Docs"
ms.date: 5/22/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Reverse

## Syntax

<pre>
Text.Reverse(<b>text</b> as nullable text) as nullable text
</pre>

## About
Reverses the provided `text`.

## Example 1
Reverse the text "123".

```powerquery-m
Text.Reverse("123")
```

`"321"`

