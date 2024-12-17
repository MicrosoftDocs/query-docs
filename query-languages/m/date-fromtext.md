---
description: "Learn more about: Date.FromText"
title: "Date.FromText"
ms.subservice: m-source
---
# Date.FromText

## Syntax

<pre>
Date.FromText(<b>text</b> as nullable text, optional <b>options</b> as any) as nullable date
</pre>
  
## About

Creates a date value from a textual representation.

* `text`: A text value to covert to a date.

* `options`: An optional `record` that can be provided to specify additional properties. The `record` can contain the following fields:

  * `Format`: A `text` value indicating the format to use. For more details, go to [Standard date and time format strings](standard-date-and-time-format-strings.md) and [Custom date and time format strings](custom-date-and-time-format-strings.md). Omitting this field or providing `null` results in parsing the date using a best effort.
  * `Culture`: When `Format` isn't null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` can also be a text value. This has the same behavior as if `options = [Format = null, Culture = options]`.

## Example 1

Convert `"2010-12-31"` into a `date` value.

**Usage**

```powerquery-m
Date.FromText("2010-12-31")
```

**Output**

`#date(2010, 12, 31)`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
Date.FromText("30 Dez 2010", [Format="dd MMM yyyy", Culture="de-DE"])
```

**Output**

`#date(2010, 12, 30)`

## Example 3

Find the date in the Gregorian calendar that corresponds to the beginning of 1400 in the Hijri calendar.

**Usage**

```powerquery-m
Date.FromText("1400", [Format="yyyy", Culture="ar-SA"])
```

**Output**

`#date(1979, 11, 20)`

## Example 4

Convert the Italian text dates with abbreviated months in the Posted Date column to date values.

**Usage**

```powerquery-m
let
    Source = #table(type table [Account Code = text, Posted Date = text, Sales = number],
    {
        {"US-2004", "20 gen. 2023", 580},
        {"CA-8843", "18 lug. 2024", 280},
        {"PA-1274", "12 gen. 2023", 90},
        {"PA-4323", "14 apr. 2023", 187},
        {"US-1200", "14 dic. 2023", 350},
        {"PTY-507", "4 giu. 2024", 110}
    }),
    #"Converted Date" = Table.TransformColumns(
        Source, 
        {"Posted Date", each Date.FromText(_, [Culture = "it-IT"]), type date}
    )
in
    #"Converted Date"
```

**Output**

```powerquery-m
#table(type table [Account Code = text, Posted Date = date, Sales = number],
{
    {"US-2004", #date(2023, 1, 20), 580},
    {"CA-8843", #date(2024, 7, 18), 280},
    {"PA-1274", #date(2023, 1, 12), 90},
    {"PA-4323", #date(2023, 4, 14), 187},
    {"US-1200", #date(2023, 12, 14), 350},
    {"PTY-507", #date(2024, 6, 4), 110}
})
```

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
