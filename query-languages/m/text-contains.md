---
description: "Learn more about: Text.Contains"
title: "Text.Contains"
---
# Text.Contains

## Syntax

<pre>
Text.Contains(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical
</pre>
  
## About

Detects whether `text` contains the value `substring`. Returns true if the value is found. This function doesn't support wildcards or regular expressions.

The optional argument `comparer` can be used to specify case-insensitive or culture and locale-aware comparisons. The following built-in comparers are available in the formula language:

* [Comparer.Ordinal](/powerquery-m/comparer-ordinal): Used to perform a case-sensitive ordinal comparison
* [Comparer.OrdinalIgnoreCase](/powerquery-m/comparer-ordinalignorecase): Used to perform a case-insensitive ordinal comparison
* [Comparer.FromCulture](/powerquery-m/comparer-fromculture): Used to perform a culture-aware comparison

If the first argument is null, this function returns null.

All characters are treated literally. For example, "DR", " DR", "DR ", and " DR " aren't considered equal to each other.

## Example 1

Find if the text "Hello World" contains "Hello".

**Usage**

```powerquery-m
Text.Contains("Hello World", "Hello")
```

**Output**

`true`

## Example 2

Find if the text "Hello World" contains "hello".

**Usage**

```powerquery-m
Text.Contains("Hello World", "hello")
```

**Output**

`false`

## Example 3

Find if the text "Hello World" contains "hello", using a case-insensitive comparer.

**Usage**

```powerquery-m
Text.Contains("Hello World", "hello", Comparer.OrdinalIgnoreCase)
```

**Output**

`true`

## Example 4

Find the rows in the provided table where the account codes contain an "A-", a "7", or both.

**Usage**

```powerquery-m
let
    // Sample input table
    TableSource = #table(type table [Account Code = text, Posted Date = date, Sales = number],
    {
        {"US-2004", #date(2023,1,20), 580},
        {"CA-8843", #date(2023,7,18), 280},
        {"PA-1274", #date(2022,1,12), 90},
        {"PA-4323", #date(2023,4,14), 187},
        {"US-1200", #date(2022,12,14), 350},
        {"PTY-507", #date(2023,6,4), 110}
    }),
    #"Filtered rows" = Table.SelectRows(
        TableSource, 
        each Text.Contains([Account Code], "A-") or
            Text.Contains([Account Code], "7"))
in
    #"Filtered rows"
```

**Output**

```powerquery-m
#table(type table [Account Code = text, Posted Date = date, Sales = number],
    {
        {"CA-8843", #date(2023,7,18), 280},
        {"PA-1274", #date(2022,1,12), 90},
        {"PA-4323", #date(2023,4,14), 187},
        {"PTY-507", #date(2023,6,4), 110}
    })
```
