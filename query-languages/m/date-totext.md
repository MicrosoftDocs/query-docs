---
title: "Date.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.ToText
`Date.ToText(**date** as nullable date, optional **format** as nullable text, optional **culture** as nullable text) as nullable text`

## About
Returns a textual representation of `date`, the Date value, `date`. This function takes in an optional format parameter `format`. For a complete list of supported formats, please refer to the Library specification document.

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







