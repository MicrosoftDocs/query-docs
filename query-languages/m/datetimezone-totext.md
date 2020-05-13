---
title: "DateTimeZone.ToText | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTimeZone.ToText

## Syntax

<pre>
DateTimeZone.ToText(<b>dateTimeZone</b> as nullable datetimezone, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About  
Returns a textual representation of `dateTimeZone`. An optional `format` may be provided to customize the formatting of the text. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get a textual representation of #datetimezone(2011, 12, 31, 11, 56, 2, 8, 0).

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 8, 0))
```

`"12/31/2010 11:56:02 AM +08:00"`

## Example 2
Get a textual representation of #datetimezone(2010, 12, 31, 11, 56, 2, 10, 12) with format option.

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 11, 56, 2, 10, 12), "yyyy/MM/ddThh:mm:sszzz")
```

`"2010/12/31T11:56:02+10:12"`
