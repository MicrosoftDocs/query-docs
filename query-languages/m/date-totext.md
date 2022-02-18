---
description: "Learn more about: Date.ToText"
title: "Date.ToText | Microsoft Docs"
ms.date: 2/16/2022
ms.service: powerquery

ms.reviewer: dougklo
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.ToText

## Syntax

<pre>
Date.ToText(<b>date</b> as nullable date, optional <b>options</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About

Returns a textual representation of `date`. An optional `record` parameter, `options`, may be provided to specify additional properties. `culture` is only used for legacy workflows (see below). The `record` can contain the following fields:

* `Format`:A `text` value indicating the format to use. Go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105.

   Omitting this field or providing `null` will result in formatting the date using the default defined by `Culture`.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` and `culture` may also be text values. This has the same behavior as if `options = [Format = options, Culture = culture]`.

## Example 1

Convert `#date(2010, 12, 31)` into a `text` value. *Result output may vary depending on current culture.*

```powerquery-m
Date.ToText(#date(2010, 12, 31))
```

`"12/31/2010"`

## Example 2

Convert using a custom format and the German culture.

```powerquery-m
Date.ToText(#date(2010, 12, 31), [Format="dd MMM yyyy", Culture="de-DE"])
```

`"31 Dez 2010"`

## Example 3

Find the year in the Hijri calendar that corresponds to January 1st, 2000 in the Gregorian calendar.

```powerquery-m
Date.ToText(#date(2000, 1, 1), [Format="yyyy", Culture="ar-SA"])
```

`"1420"`
