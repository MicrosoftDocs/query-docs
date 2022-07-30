---
description: "Learn more about: DateTime.FromText"
title: "DateTime.FromText"
ms.date: 6/24/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.FromText

## Syntax

<pre>
DateTime.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable datetime
</pre>
  
## About

Creates a `datetime` value from a textual representation, `text`. An optional `record` parameter, `options`, may be provided to specify additional properties. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105. Omitting this field or providing `null` will result in parsing the date using a best effort.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` may also be a text value. This has the same behavior as if `options = [Format = null, Culture = options]`.

## Example 1

Convert `"2010-12-31T01:30:00"` into a datetime value.

**Usage**

```powerquery-m
DateTime.FromText("2010-12-31T01:30:25")
```

**Output**

`#datetime(2010, 12, 31, 1, 30, 25)`

## Example 2

Convert `"2010-12-31T01:30:00.121212"` into a datetime value.

**Usage**

```powerquery-m
DateTime.FromText("30 Dez 2010 02:04:50.369730", [Format="dd MMM yyyy HH:mm:ss.ffffff", Culture="de-DE"])
```

**Output**

`#datetime(2010, 12, 30, 2, 4, 50.36973)`

## Example 3

Convert `"2010-12-31T01:30:00"` into a datetime value.

**Usage**

```powerquery-m
DateTime.FromText("2000-02-08T03:45:12Z", [Format="yyyy-MM-dd'T'HH:mm:ss'Z'", Culture="en-US"])
```

**Output**

`#datetime(2000, 2, 8, 3, 45, 12)`

## Example 4

Convert `"20101231T013000"` into a datetime value.

**Usage**

```powerquery-m
DateTime.FromText("20101231T013000", [Format="yyyyMMdd'T'HHmmss", Culture="en-US"])
```

**Output**

`#datetime(2010, 12, 31, 1, 30, 0)`
