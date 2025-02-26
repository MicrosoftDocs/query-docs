---
description: "Learn more about: Text.TrimEnd"
title: "Text.TrimEnd"
ms.subservice: m-source
---
# Text.TrimEnd

## Syntax

<pre>
Text.TrimEnd(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all trailing characters from the specified `text`. By default, all the trailing whitespace characters are removed.

* `text`: The text from which the trailing characters are to be removed.
* `trim`: Overrides the whitespace characters that are trimmed by default. This parameter can either be a single character or a list of single characters. Each trailing trim operation stops when a non-trimmed character is encountered.

## Example 1

Remove trailing whitespace from "     a b c d    ".

**Usage**

```powerquery-m
Text.TrimEnd("     a b c d    ")
```

**Output**

<pre>
"     a b c d"
</pre>

## Example 2

Remove trailing zeroes from a text representation of a padded floating point number.

**Usage**

```powerquery-m
Text.TrimEnd("03.487700000", "0")
```

**Output**

`"03.4877"`

## Example 3

Remove the trailing padding characters from a fixed-width account name.

**Usage**

```powerquery-m
let
    Source = #table(type table [Name = text, Account Name= text, Interest = number],
    {
        {"Bob", "US-847263****@", 2.8410},
        {"Leslie", "FR-4648****@**", 3.8392},
        {"Ringo", "DE-2046790@***", 12.6600}
    }),
    #"Trimmed Account" = Table.TransformColumns(Source, {"Account Name", each Text.TrimEnd(_, {"*", "@"})})
in
    #"Trimmed Account"
```

**Output**

```powerquery-m
#table(type table [Name = text, Account Name = text, Interest = number],
    {
        {"Bob", "US-847263", 2.841},
        {"Leslie", "FR-4648", 3.8392},
        {"Ringo", "DE-2046790", 12.66}
    }),

```
