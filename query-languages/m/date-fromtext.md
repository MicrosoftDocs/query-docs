---
title: "Date.FromText | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.FromText

## Syntax

<pre>
Date.FromText(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable date 
</pre>
  
## About  
Creates a `date` value from a textual representation, `text`, following ISO 8601 format standard. <ul> <li> <code>Date.FromText("2010-02-19") </code> // Date, yyyy-MM-dd </li> </ul>

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
