---
description: "Learn more about: DateTime.FromText"
title: "DateTime.FromText | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.FromText

## Syntax

<pre>
DateTime.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable datetime
</pre>
  
## About  
Creates a `datetime` value from a textual representation, `text`, following ISO 8601 format standard. An optional `options` may also be provided (for example, "en-US").

* `DateTime.FromText("2010-12-31T01:30:00") ` // yyyy-MM-ddThh:mm:ss

## Example 1
Convert `"2010-12-31T01:30:25"` into a datetime value.

```powerquery-m
DateTime.FromText("2010-12-31T01:30:25")
```

`#datetime(2010, 12, 31, 1, 30, 25)`

## Example 2
Convert `"2010-12-31T01:30"` into a datetime value.

```powerquery-m
DateTime.FromText("2010-12-31T01:30")
```

`#datetime(2010, 12, 31, 1, 30, 0)`

## Example 3
Convert `"20101231T013025"` into a datetime value.

```powerquery-m
DateTime.FromText("20101231T013025")
```

`#datetime(2010, 12, 31, 1, 30, 25)`

## Example 4
Convert `"20101231T01:30:25"` into a datetime value.

```powerquery-m
DateTime.FromText("20101231T01:30:25")
```

`#datetime(2010, 12, 31, 1, 30, 25)`

## Example 5
Convert `"20101231T01:30:25.121212"` into a datetime value.

```powerquery-m
DateTime.FromText("20101231T01:30:25.121212")
```

`#datetime(2010, 12, 31, 1, 30, 25.121212)`
