---
description: "Learn more about: Text.TrimStart"
title: "Text.TrimStart"
---
# Text.TrimStart

## Syntax

<pre>
Text.TrimStart(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all leadling characters from the specified `text`. By default, all the leading whitespace characters are removed.

* `text`: The text from which the leading characters are to be removed.
* `trim`" Overrides the whitespace characters that are trimmed by default. This parameter can either be a single character or a list of single characters. Each leading trim operation stops when a non-trimmed character is encountered.

## Example 1

Remove leading whitespace from " a b c d ".

Usage**

```powerquery-m
Text.TrimStart("   a b c d    ")
```

**Output**

<pre>
"a b c d    "
</pre>

## Example 2

Remove leading zeroes from the text representation of a number.

**Usage**

```powerquery-m
Text.TrimStart("0000056.420", "0")
```

**Output**

`"56.420"`

## Example 3

Remove the leading padding characters from a fixed width account name.

**Usage**

```powerquery-m
let
    Source = #table(type table [Name = text, Account Name= text, Interest = number],
    {
        {"Bob", "@****847263-US", 2.8410},
        {"Leslie", "@******4648-FR", 3.8392},
        {"Ringo", "@*****24679-DE", 12.6600}
    }),
    #"Trimmed Account" = Table.TransformColumns(Source, {{"Account Name", each Text.TrimStart(_, {"*", "@"})}})
in
    #"Trimmed Account"
```

**Output**

```powerquery-m
#table(type table [Name = text, Account Name = text, Interest = number],
    {
        {"Bob", "847263-US", 2.841},
        {"Leslie", "4648-FR", 3.8392},
        {"Ringo", "2046790-DE", 12.66}
    }),

