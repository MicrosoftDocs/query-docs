---
title: "DateTime.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.ToText

## Syntax

<pre>DateTime.ToText(**dateTime** as nullable datetime, optional **format** as nullable text, optional **culture** as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `dateTime`, the datetime value, `dateTime`. This function takes in an optional format parameter `format`. For a complete list of supported formats, please refer to the Library specification document.

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


