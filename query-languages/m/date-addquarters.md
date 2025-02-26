---
description: "Learn more about: Date.AddQuarters"
title: "Date.AddQuarters"
ms.subservice: m-source
---
# Date.AddQuarters

## Syntax

<pre>
Date.AddQuarters(<b>dateTime</b> as any, <b>numberOfQuarters</b> as number) as any
</pre>

## About

Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfQuarters` quarters to the `datetime` value `dateTime`.

* `dateTime`: The `date`, `datetime`, or `datetimezone` value to which quarters are being added.
* `numberOfQuarters`: The number of quarters to add.

## Example 1

Add 1 quarter to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

**Usage**

```powerquery-m
Date.AddQuarters(#date(2011, 5, 14), 1)
```

**Output**

`#date(2011, 8, 14)`

## Related content

* [#date](sharpdate.md)
* [#datetime](sharpdatetime.md)
* [#datetimezone](sharpdatetimezone.md)
