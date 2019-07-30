---
title: "Date.From | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.From

## Syntax

<pre>
Date.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable date 
</pre>
  
## About  
Returns a `date` value from the given `value`. If the given `value` is `null`, `Date.From` returns `null`. If the given `value` is `date`, `value` is returned. Values of the following types can be converted to a `date` value: <ul> <li><code>text</code>: A <code>date</code> value from textual representation. See <code>Date.FromText</code> for details.</li> <li><code>datetime</code>: The date component of the <code>value</code>.</li> <li><code>datetimezone</code>: The date component of the local datetime equivalent of <code>value</code>.</li> <li><code>number</code>: The date component of the datetime equivalent the OLE Automation Date expressed by <code>value</code>.</li> </ul> If <code>value</code> is of any other type, an error is returned.

## Example 1
Convert `43910` to a `date` value.

```powerquery-m
Date.From(43910)
```

`#date(2020, 3, 20)`


## Example 2
Convert `#datetime(1899, 12, 30, 06, 45, 12)` to a `date` value.

```powerquery-m
Date.From(#datetime(1899, 12, 30, 06, 45, 12))
```

`#date(1899, 12, 30)`
