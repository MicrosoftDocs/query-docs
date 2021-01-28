---
description: "Learn more about: Time.FromText"
title: "Time.FromText | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Time.FromText

## Syntax

<pre>
Time.FromText(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable time
</pre>
  
## About  
Creates a `time` value from a textual representation, `text`, following ISO 8601 format standard. An optional `culture` may also be provided (for example, "en-US"). <ul> <li> <code>Time.FromText("12:34:12")</code> // Time, hh:mm:ss </li> <li> <code>Time.FromText("12:34:12.1254425")</code> // hh:mm:ss.nnnnnnn </li> </ul>

## Example 1
Convert `"10:12:31am"` into a Time value.

```powerquery-m
Time.FromText("10:12:31am")
```

`#time(10, 12, 31)`

## Example 2
Convert `"1012"` into a Time value.

```powerquery-m
Time.FromText("1012")
```

`#time(10, 12, 00)`

## Example 3
Convert `"10"` into a Time value.

```powerquery-m
Time.FromText("10")
```

`#time(10, 00, 00)`
