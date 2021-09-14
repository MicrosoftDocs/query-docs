---
description: "Learn more about: DateTimeZone.FromText"
title: "DateTimeZone.FromText | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTimeZone.FromText

## Syntax

<pre>
DateTimeZone.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable datetimezone
</pre>
  
## About  
Creates a `datetimezone` value from a textual representation, `text`, following ISO 8601 format standard. An optional `options` may also be provided (for example, "en-US").

* `DateTimeZone.FromText("2010-12-31T01:30:00-08:00") ` // yyyy-MM-ddThh:mm:ssZ

## Example 1
Convert `"2010-12-31T01:30:00-08:00"` into a datetimezone value.

```powerquery-m
DateTimeZone.FromText("2010-12-31T01:30:00-08:00")
```

`#datetimezone(2010, 12, 31, 1, 30, 0, -8, 0)`

## Example 2
Convert `"2010-12-31T01:30:00.121212-08:00"` into a datetimezone value.

```powerquery-m
DateTimeZone.FromText("2010-12-31T01:30:00.121212-08:00")
```

`#datetimezone(2010, 12, 31, 1, 30, 0.121212, -8, 0)`

## Example 3
Convert `"2010-12-31T01:30:00Z"`into a datetimezone value.

```powerquery-m
DateTimeZone.FromText("2010-12-31T01:30:00Z")
```

`#datetimezone(2010, 12, 31, 1, 30, 0, 0, 0)`

## Example 4
Convert `"20101231T013000+0800"` into a datetimezone value.

```powerquery-m
DateTimeZone.FromText("20101231T013000+0800")
```

`#datetimezone(2010, 12, 31, 1, 30, 0, 8, 0)`
