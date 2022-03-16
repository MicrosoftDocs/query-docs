---
description: "Learn more about: Time.ToText"
title: "Time.ToText | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: dougklo
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.ToText

## Syntax

<pre>
Time.ToText(<b>time</b> as nullable time, optional <b>options</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About

Returns a textual representation of `time`. An optional `record` parameter, `options`, may be provided to specify additional properties. `culture` is only used for legacy workflows (see below). The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. Go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105.

   Omitting this field or providing `null` will result in formatting the date using the default defined by `Culture`.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` and `culture` may also be text values. This has the same behavior as if `options = [Format = options, Culture = culture]`.

## Example 1

Convert `#time(01, 30, 25)` into a `text` value. *Result output may vary depending on current culture.*

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2))
```

**Output**

`"11:56 AM"`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2), [Format="hh:mm", Culture="de-DE"])
```

**Output**

`"11:56"`

## Example 3

Convert using standard time format.

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2), [Format="T", Culture="de-DE"])
```

**Output**

`"11:56:02"`
