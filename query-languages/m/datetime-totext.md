---
title: "DateTime.ToText | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTime.ToText

## Syntax

<pre>
DateTime.ToText(<b>dateTime</b> as nullable datetime, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `dateTime`, the datetime value, `dateTime`. This function takes in an optional format parameter `format`. For a complete list of supported formats, refer to the Library specification document. An optional `culture` may also be provided (for example, "en-US").

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


