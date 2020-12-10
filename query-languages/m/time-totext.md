---
title: "Time.ToText | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.ToText

## Syntax

<pre>
Time.ToText(<b>time</b> as nullable time, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `time`. An optional `format` may be provided to customize the formatting of the text. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get a textual representation of #time(11, 56, 2).

```powerquery-m
Time.ToText(#time(11, 56, 2))
``` 

`
"11:56 AM"
` 

## Example 2
Get a textual representation of #time(11, 56, 2) with format option.

```powerquery-m
Time.ToText(#time(11, 56, 2), "hh:mm")
``` 

`
"11:56"
`
