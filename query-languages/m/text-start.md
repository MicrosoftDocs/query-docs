---
description: "Learn more about: Text.Start"
title: "Text.Start"
---
# Text.Start

## Syntax

<pre>
Text.Start(<b>text</b> as nullable text, <b>count</b> as number) as nullable text
</pre>
  
## About

Returns the first `count` characters of `text` as a text value.

## Example 1

Get the first 5 characters of "Hello, World".

**Usage**

```powerquery-m
Text.Start("Hello, World", 5)
```

**Output**

`"Hello"`

## Example 2

Get the first four characters of the first name and the first three characters of the last name to create an individual's username that also includes the company website.

**Usage**

```powerquery-m
let
    Source = #table(type table [First Name = text, Last Name = text],
    {
        {"Douglas", "Elis"},
        {"Ana", "Jorayew"},
        {"Rada", "Mihaylova"}
    }),
    Username = Table.AddColumn(
        Source,
        "Username", 
        each Text.Combine({
            Text.Start([First Name], 4),
            Text.Start([Last Name], 3),
            "@contoso.com"
        })
    )
in
    Username
```

**Output**

```powerquery-m
#table(type table [First Name = text, Last Name = text, Username = text],
{
    {"Doug", "J", "Elis", "DougEli@contoso.com"},
    {"Anna", "M", "Jorayew", "AnaJor@contoso.com"},
    {"Rada", null, "Mihaylova", "RadaMih@contoso.com"}
})
```
