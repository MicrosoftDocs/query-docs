---
description: "Learn more about: Time.FromText"
title: "Time.FromText | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.FromText

## Syntax

<pre>
Time.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable time
</pre>
  
## About

Creates a `time` value from a textual representation, `text`, following ISO 8601 format standard. An optional `options` may also be provided (for example, "en-US").

* `Time.FromText("12:34:12")` // Time, hh:mm:ss
* `Time.FromText("12:34:12.1254425")` // hh:mm:ss.nnnnnnn

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
