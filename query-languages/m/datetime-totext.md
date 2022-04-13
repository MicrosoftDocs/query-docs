---
description: "Learn more about: DateTime.ToText"
title: "DateTime.ToText | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: dougklo
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

Returns a textual representation of `dateTime`. An optional `record` parameter, `options`, may be provided to specify additional properties. `culture` is only used for legacy workflows. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105.

   Omitting this field or providing `null` will result in formatting the date using the default defined by `Culture`.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` and `culture` may also be text values. This has the same behavior as if `options = [Format = options, Culture = culture]`.

## Example 1

Convert `#datetime(2010, 12, 31, 01, 30, 25)` into a `text` value. *Result output may vary depending on current culture.*

**Usage**

```powerquery-m
DateTime.ToText(#datetime(2010, 12, 31, 01, 30, 25))
```

**Output**

`"12/31/2010 1:30:25 AM"`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
DateTime.ToText(#datetime(2010, 12, 30, 2, 4, 50.36973), [Format="dd MMM yyyy HH:mm:ss.ffffff", Culture="de-DE"])
```

**Output**

`"30 Dez 2010 02:04:50.369730"`

## Example 3

Convert using the ISO 8601 pattern.

**Usage**

```powerquery-m
DateTime.ToText(#datetime(2000, 2, 8, 3, 45, 12),[Format="yyyy-MM-dd'T'HH:mm:ss'Z'", Culture="en-US"])
```

**Output**

`"2000-02-08T03:45:12Z"`
