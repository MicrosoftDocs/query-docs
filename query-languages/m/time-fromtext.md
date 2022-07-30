---
description: "Learn more about: Time.FromText"
title: "Time.FromText | Microsoft Docs"
ms.date: 6/24/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Time.FromText

## Syntax

<pre>
Time.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable time
</pre>
  
## About

Creates a `time` value from a textual representation, `text`. An optional `record` parameter, `options`, may be provided to specify additional properties. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to https://go.microsoft.com/fwlink/?linkid=2180104 and https://go.microsoft.com/fwlink/?linkid=2180105. Omitting this field or providing `null` will result in parsing the time using a best effort.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"tt"` is `"AM" or "PM"`, while in `"ar-EG"` `"tt"` is `"ص" or "م"`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` may also be a text value. This has the same behavior as if `options = [Format = null, Culture = options]`.

## Example 1

Convert `"10:12:31am"` into a Time value.

**Usage**

```powerquery-m
Time.FromText("10:12:31am")
```

**Output**

`#time(10, 12, 31)`

## Example 2

Convert `"1012"` into a Time value.

**Usage**

```powerquery-m
Time.FromText("1012")
```

**Output**

`#time(10, 12, 00)`

## Example 3

Convert `"10"` into a Time value.

**Usage**

```powerquery-m
Time.FromText("10")
```

**Output**

`#time(10, 00, 00)`
