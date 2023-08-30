---
description: "Learn more about: Date.FromText"
title: "Date.FromText"
---
# Date.FromText

## Syntax

<pre>
Date.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable date
</pre>
  
## About

Creates a `date` value from a textual representation, `text`. An optional `record` parameter, `options`, may be provided to specify additional properties. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105. Omitting this field or providing `null` will result in parsing the date using a best effort.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` may also be a text value. This has the same behavior as if `options = [Format = null, Culture = options]`.

## Example 1

Convert `"2010-12-31"` into a `date` value.

**Usage**

```powerquery-m
Date.FromText("2010-12-31")
```

**Output**

`#date(2010, 12, 31)`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
Date.FromText("30 Dez 2010", [Format="dd MMM yyyy", Culture="de-DE"])
```

**Output**

`#date(2010, 12, 30)`

## Example 3

Find the date in the Gregorian calendar that corresponds to the beginning of 1400 in the Hijri calendar.

**Usage**

```powerquery-m
Date.FromText("1400", [Format="yyyy", Culture="ar-SA"])
```

**Output**

`#date(1979, 11, 20)`
