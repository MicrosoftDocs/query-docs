---
description: "Learn more about: Date.MonthName"
title: "Date.MonthName"
---
# Date.MonthName

## Syntax

<pre>
Date.MonthName(<b>date</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About

Returns the name of the month component for the provided `date`. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the month name.

**Usage**

```powerquery-m
Date.MonthName(#datetime(2011, 12, 31, 5, 0, 0), "en-US")
```

**Output**

`"December"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
