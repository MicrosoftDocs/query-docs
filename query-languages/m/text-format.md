---
title: "Text.Format | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Format

## Syntax

<pre>
Text.Format(<b>formatString</b> as text, <b>arguments</b> as any, optional <b>culture</b> as nullable text) as text
</pre> 
  
## About  
Returns formatted text that is created by applying `arguments` from a list or record to a format string `formatString`. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Format a list of numbers.

```powerquery-m
Text.Format("#{0}, #{1}, and #{2}.", {17, 7, 22})
```

`"17, 7, and 22."`

## Example 2
Format different data types from a record according to United States English culture.

```powerquery-m
Text.Format(
    "The time for the #[distance] km run held in #[city] on #[date] was #[duration].",
    [
        city = "Seattle",
        date = #date(2015, 3, 10),
        duration = #duration(0, 0, 54, 40),
        distance = 10
    ],
    "en-US"

```

`"The time for the 10 km run held in Seattle on 3/10/2015 was 00:54:40."`
