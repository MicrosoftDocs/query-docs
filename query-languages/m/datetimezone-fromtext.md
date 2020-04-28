---
title: "DateTimeZone.FromText | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTimeZone.FromText

## Syntax

<pre>
DateTimeZone.FromText(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable datetimezone
</pre>
  
## About  
Creates a `datetimezone` value from a textual representation, `text`, following ISO 8601 format standard. An optional `culture` may also be provided (for example, "en-US"). <ul> <li> <code>DateTimeZone.FromText("2010-12-31T01:30:00-08:00") </code> // yyyy-MM-ddThh:mm:ssZ </li> </ul>

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

