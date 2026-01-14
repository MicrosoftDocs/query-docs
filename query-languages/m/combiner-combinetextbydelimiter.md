---
description: "Learn more about: Combiner.CombineTextByDelimiter"
title: "Combiner.CombineTextByDelimiter"
ms.subservice: m-source
ms.topic: reference
---
# Combiner.CombineTextByDelimiter

## Syntax

<pre>
Combiner.CombineTextByDelimiter(<b>delimiter</b> as text, optional <b>quoteStyle</b> as nullable number) as function
</pre>

## About

Returns a function that combines a list of text values into a single text value using the specified delimiter.

## Example 1

Combine a list of text values using a semicolon delimiter.

**Usage**

```powerquery-m
Combiner.CombineTextByDelimiter(";")({"a", "b", "c"})
```

**Output**

`"a;b;c"`

## Example 2

Combine the text of two columns using a comma delimiter and CSV-style quoting.

**Usage**

```powerquery-m
let
    Source = #table(
        type table [Column1 = text, Column2 = text],
        {{"a", "b"}, {"c", "d,e,f"}}
    ),
    Merged = Table.CombineColumns(
        Source,
        {"Column1", "Column2"},
        Combiner.CombineTextByDelimiter(",", QuoteStyle.Csv),
        "Merged"
    )
in
    Merged
```

**Output**

```powerquery-m
#table(
    type table [Merged = text],
    {{"a,b"}, {"c,""d,e,f"""}}
)
```
