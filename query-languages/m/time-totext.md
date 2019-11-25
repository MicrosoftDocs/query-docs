---
title: "Time.ToText | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Time.ToText

## Syntax

<pre>
Time.ToText(<b>time</b> as nullable time, optional <b>format</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About
Returns a textual representation of `time`, the Time value, `time`. This function takes in an optional format parameter `format`. For a complete list of supported formats, please refer to the Library specification document.

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
