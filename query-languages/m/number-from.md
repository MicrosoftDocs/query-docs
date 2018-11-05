---
title: "Number.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.From

## Syntax

<pre>
Number.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About
Returns a `number` value from the given `value`. If the given `value` is `null`, `Number.From` returns `null`. If the given `value` is `number`, `value` is returned. Values of the following types can be converted to a `number` value: <ul> <li>`text`: A `number` value from textual representation. Common text formats are handled ("15", "3,423.10", "5.0E-10"). See `Number.FromText` for details.</li> <li>`logical`: 1 for `true`, 0 for `false`.</li> <li>`datetime`: A double-precision floating-point number that contains an OLE Automation date equivalent.</li> <li>`datetimezone`: A double-precision floating-point number that contains an OLE Automation date equivalent of the local date and time of `value`.</li> <li>`date`: A double-precision floating-point number that contains an OLE Automation date equivalent.</li> <li>`time`: Expressed in fractional days.</li> <li>`duration`: Expressed in whole and fractional days.</li> </ul> If `value` is of any other type, an error is returned.

## Example 1
Get the `number` value of `"4"`.

```
powerquery-mNumber.From("4")
```

`4`

## Example 2
Get the `number` value of `#datetime(2020, 3, 20, 6, 0, 0)`.

```powerquery-m
Number.From(#datetime(2020, 3, 20, 6, 0, 0))
```

`43910.25`

## Example 3
Get the `number` value of `"12.3%"`.

```powerquery-m
Number.From("12.3%")
```

`0.123`
