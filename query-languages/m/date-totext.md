---
title: "Date.ToText | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.ToText

## Syntax

<pre>
Date.ToText(<b>date</b> as nullable date, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `date`. An optional `format` may be provided to customize the formatting of the text. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get a textual representation of #date(2010, 12, 31).

```powerquery-m
Date.ToText(#date(2010, 12, 31))
```

`"12/31/2010"`


## Example 2
Get a textual representation of #date(2010, 12, 31) with format option.

```powerquery-m
Date.ToText(#date(2010, 12, 31), "yyyy/MM/dd")
```

`"2010/12/31"`







