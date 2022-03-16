---
description: "Learn more about: Date.From"
title: "Date.From | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: dougklo
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.From

## Syntax

<pre>
Date.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable date
</pre>
  
## About

Returns a `date` value from the given `value`. An optional `culture`> may also be provided (for example, "en-US"). If the given `value` is `null`, `Date.From` returns `null`. If the given `value` is `date`, `value` is returned. Values of the following types can be converted to a `date` value:

* `text`: A `date` value from textual representation. Go to [Date.FromText](date-fromtext.md) for details.
* `datetime`: The date component of the `value`.
* `datetimezone`: The date component of the local datetime equivalent of `value`.
* `number`: The date component of the datetime equivalent to the OLE Automation Date expressed by `value`.

If `value` is of any other type, an error is returned.

## Example 1

Convert `43910` to a `date` value.

**Usage**

```powerquery-m
Date.From(43910)
```

**Output**

`#date(2020, 3, 20)`

## Example 2

Convert `#datetime(1899, 12, 30, 06, 45, 12)` to a `date` value.

**Usage**

```powerquery-m
Date.From(#datetime(1899, 12, 30, 06, 45, 12))
```

**Output**

`#date(1899, 12, 30)`
