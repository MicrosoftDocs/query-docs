---
description: "Learn more about: Text.From"
title: "Text.From"
ms.subservice: m-source
ms.topic: reference
---
# Text.From

## Syntax

<pre>
Text.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Returns the text representation of a specified value.

* `value`: The value to convert to text. The value can be a `number`, `date`, `time`, `datetime`, `datetimezone`, `logical`, `duration`, or `binary` value. If the given value is `null`, this function returns `null`.
* `culture`: (Optional) The culture to use when converting the value to text (for example, "en-US").

## Example 1

Create a text value from the number 3.

**Usage**

```powerquery-m
Text.From(3)
```

**Output**

`"3"`

## Example 2

Get the text equivalent of the specified date and time.

**Usage**

```powerquery-m
Text.From(#datetime(2024, 6, 24, 14, 32, 22))
```

**Output**

`"6/24/2024 2:32:22 PM"`

## Example 3

Get the German text equivalent of the specified date and time.

**Usage**

```powerquery-m
Text.From(#datetime(2024, 6, 24, 14, 32, 22), "de-DE")
```

**Output**

`"24.06.2024 14:32:22"`

## Example 4

Get a binary value from text encoded as hexadecimal and change the value back to text.

**Usage**

```powerquery-m
Text.From(Binary.FromText("10FF", BinaryEncoding.Hex))
```

**Output**

`"EP8="`

## Example 5

Get the rows in the table that contain data for France and convert the dates to text using the French culture.

**Usage**

```powerquery-m
let
    Source = #table(type table [Company ID = text, Country = text, Date = date],
    {
        {"JS-464", "USA", #date(2024, 3, 24)},
        {"LT-331", "France", #date(2024, 10, 5)},
        {"XE-100", "USA", #date(2024, 5, 21)},
        {"RT-430", "Germany", #date(2024, 1,18)},
        {"LS-005", "France", #date(2023, 12, 31)},
        {"UW-220", "Germany", #date(2024, 2, 25)}
    }),
    #"Convert Dates" = Table.TransformColumns(
        Table.SelectRows(Source, each [Country] = "France"),
        {"Date", each Text.From(_, "fr-FR")}
    )
in
    #"Convert Dates"
```

**Output**

```powerquery-m
#table(type table [Company ID = text, Country = text, Date = text],
{
    {"LT-331", "France", "05/10/2024"},
    {"LS-005", "France", "31/12/2023"}
})
```

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard numeric format strings](standard-numeric-format-strings.md)
* [Custom numeric format strings](custom-numeric-format-strings.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
