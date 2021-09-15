---
description: "Learn more about: Date.FromText"
title: "Date.FromText | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.FromText

## Syntax

<pre>
Date.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable date 
</pre>
  
## About  
Creates a `date` value from a textual representation, `text`, following ISO 8601 format standard. An optional `options` may also be provided (for example, "en-US").

* `Date.FromText("2010-02-19") ` // Date, yyyy-MM-dd

## Example 1
Convert `"December 31, 2010"` into a date value.

```powerquery-m
Date.FromText("2010-12-31")
```

`#date(2010, 12, 31)`

## Example 2
Convert `"December 31, 2010"` into a date value, with a different format

```powerquery-m
Date.FromText("2010, 12, 31")
```

`#date(2010, 12, 31)`

## Example 3
Convert `"December, 2010"` into a date value.

```powerquery-m
Date.FromText("2010, 12")
```

`#date(2010, 12, 1)`

## Example 4
Convert `"2010"` into a date value.

```powerquery-m
Date.FromText("2010")
```

`#date(2010, 1, 1)`
