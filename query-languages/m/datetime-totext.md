---
description: "Learn more about: DateTime.ToText"
title: "DateTime.ToText | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.ToText

## Syntax

<pre>
DateTime.ToText(<b>dateTime</b> as nullable datetime, optional <b>options</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `dateTime`. An optional `options` may be provided to customize the formatting of the text. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get a textual representation of #datetime(2011, 12, 31, 11, 56, 2).

```powerquery-m
DateTime.ToText(#datetime(2010, 12, 31, 11, 56, 2))
```

```powerquery-m
"12/31/2010 11:56:02 AM"
```


## Example 2

Get a textual representation of #datetime(2011, 12, 31, 11, 56, 2) with format option.

```powerquery-m
DateTime.ToText(#datetime(2010, 12, 31, 11, 56, 2), "yyyy/MM/ddThh:mm:ss")
```

```powerquery-m
"2010/12/31T11:56:02"
```
