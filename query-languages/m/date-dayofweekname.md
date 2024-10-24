---
description: "Learn more about: Date.DayOfWeekName"
title: "Date.DayOfWeekName"
---
# Date.DayOfWeekName

## Syntax

<pre>
Date.DayOfWeekName(<b>date</b> as any, optional <b>culture</b> as nullable text) as nullable text

</pre>

## About

Returns the day of the week name for the provided `date`. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the day of the week name.

**Usage**

```powerquery-m
Date.DayOfWeekName(#date(2011, 12, 31), "en-US")
```

**Output**

`"Saturday"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
