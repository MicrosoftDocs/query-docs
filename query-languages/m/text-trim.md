---
description: "Learn more about: Text.Trim"
title: "Text.Trim"
---
# Text.Trim

## Syntax

<pre>
Text.Trim(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all leading and trailing characters from the specified `text`. By default, all the leading and trailing whitespace characters are removed.

* `text`: The text from which the leading and trailing characters are to be removed.
* `trim`: Overrides the whitespace characters that are trimmed by default. This parameter can either be a single character or a list of single characters. Each leading and trailing trim operation stops when a non-trimmed character is encountered.

## Example 1

Remove leading and trailing whitespace from " a b c d ".

**Usage**

```powerquery-m
Text.Trim("     a b c d    ")
```

**Output**

`"a b c d"`

## Example 2

Remove leading and trailing zeroes from the text representation of a number.

**Usage**

```powerquery-m
Text.Trim("0000056.4200", "0")
```

**Output**

`"56.42"`

## Example 3

Remove the leading and trailing brackets from an HTML tag.

**Usage**

```powerquery-m
Text.Trim("<div/>", {"<", ">", "/"})
```

**Output**

`"div"`

## Example 4

Remove the special characters used around the pending sales status.

**Usage**

```powerquery-m
let
    Source = #table(type table [Home Sale = text, Sales Date = date, Sales Status = text],
    {
        {"1620 Ferris Way", #date(2024, 8, 22), "##@@Pending@@##"},
        {"757 1st Ave. S.", #date(2024, 3, 15), "Sold"},
        {"22303 Fillmore", #date(2024, 10, 2), "##@@Pending@@##"}
    }),
    #"Trimmed Status" = Table.TransformColumns(Source, {"Sales Status", each Text.Trim(_, {"#", "@"})})
in
    #"Trimmed Status"
```

**Output**

```powerquery-m
#table(type table [Home Sale = text, Sales Date = date, Sales Status = text],
    {
        {"1620 Ferris Way", #date(2024, 8, 22), "Pending"},
        {"757 1st Ave. S.", #date(2024, 3, 15), "Sold"},
        {"22303 Fillmore", #date(2024, 10, 2), "Pending"}
    })
```
