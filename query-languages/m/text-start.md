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

Use the first four characters of the first name and the first three characters of the last name to create an individual's email address.

**Usage**

```powerquery-m
let
    Source = #table(type table [First Name = text, Last Name = text],
    {
        {"Douglas", "Elis"},
        {"Ana", "Jorayew"},
        {"Rada", "Mihaylova"}
    }),
    EmailAddress = Table.AddColumn(
        Source,
        "Email Address", 
        each Text.Combine({
            Text.Start([First Name], 4),
            Text.Start([Last Name], 3),
            "@contoso.com"
        })
    )
in
    EmailAddress
```

**Output**

```powerquery-m
#table(type table [First Name = text, Last Name = text, Email Address = text],
{
    {"Douglas", "Elis", "DougEli@contoso.com"},
    {"Ana", "Jorayew", "AnaJor@contoso.com"},
    {"Rada", "Mihaylova", "RadaMih@contoso.com"}
})
```
