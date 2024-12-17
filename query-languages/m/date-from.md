---
description: "Learn more about: Date.From"
title: "Date.From"
ms.subservice: m-source
---
# Date.From

## Syntax

<pre>
Date.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable date
</pre>
  
## About

Returns a date value from the given value.

* `value`: The value to covert to a date. If the given value is `null`, this function returns `null`. If the given value is `date`, `value` is returned. Values of the following types can be converted to a `date` value:

  * `text`: A `date` value from textual representation. Refer to [Date.FromText](date-fromtext.md) for details.
  * `datetime`: The date component of the `value`.
  * `datetimezone`: The date component of the local datetime equivalent of `value`.
  * `number`: The date component of the datetime equivalent of a floating-point number whose integral component is the number of days before or after midnight, 30 December 1899, and whose fractional component represents the time on that day divided by 24. For example, midnight, 31 December 1899 is represented by 1.0; 6 A.M., 1 January 1900 is represented by 2.25; midnight, 29 December 1899 is represented by -1.0; and 6 A.M., 29 December 1899 is represented by -1.25. The base value is midnight, 30 December 1899. The minimum value is midnight, 1 January 0100. The maximum value is the last moment of 31 December 9999.

  If `value` is of any other type, an error is returned.

* `culture`: The culture of the given value (for example, "en-US").

## Example 1

Convert the specified date and time to a date value.

**Usage**

```powerquery-m
Date.From(#datetime(1899, 12, 30, 06, 45, 12))
```

**Output**

`#date(1899, 12, 30)`

## Example 2

Convert the specified number to a date value.

**Usage**

```powerquery-m
Date.From(43910)
```

**Output**

#date(2020, 3, 20)

## Example 3

Convert the German text dates in the Posted Date column to date values.

**Usage**

```powerquery-m
let
    Source = #table(type table [Account Code = text, Posted Date = text, Sales = number],
    {
        {"US-2004", "20 Januar 2023", 580},
        {"CA-8843", "18 Juli, 2023", 280},
        {"PA-1274", "12 Januar, 2022", 90},
        {"PA-4323", "14 April 2023", 187},
        {"US-1200", "14 Dezember, 2022", 350},
        {"PTY-507", "4 Juni, 2023", 110}
    }),
    #"Filtered rows" = Table.TransformColumns(
        Source, 
        {"Posted Date", each Date.From(_, "de-DE"), type date}
    )
in
    #"Filtered rows"
```

**Output**

```powerquery-m
#table(type table [Account Code = text, Posted Date = date, Sales = number],
{
    {"US-2004", #date(2023, 1, 20), 580},
    {"CA-8843", #date(2023, 7, 18), 280},
    {"PA-1274", #date(2022, 1, 12), 90},
    {"PA-4323", #date(2023, 4, 14), 187},
    {"US-1200", #date(2022, 12, 14), 350},
    {"PTY-507", #date(2023, 6, 4), 110}
})
```

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
