---
description: "Learn more about: Text.Combine"
title: "Text.Combine"
ms.subservice: m-source
ms.topic: reference
---
# Text.Combine

## Syntax

<pre>
Text.Combine(<b>texts</b> as list, optional <b>separator</b> as nullable text) as text
</pre>
  
## About

Returns the result of combining the list of text values, `texts`, into a single text value. Any `null` values present in `texts` are ignored. An optional `separator` used in the final combined text can be specified.

## Example 1

Combine text values "Seattle" and "WA".

**Usage**

```powerquery-m
Text.Combine({"Seattle", "WA"})
```

**Output**

`"SeattleWA"`

## Example 2

Combine text values "Seattle" and "WA", separated by a comma and a space.

**Usage**

```powerquery-m
Text.Combine({"Seattle", "WA"}, ", ")
```

**Output**

`"Seattle, WA"`

## Example 3

Combine the values "Seattle", `null`, and "WA", separated by a comma and a space. (Note that the `null` is ignored.)

**Usage**

```powerquery-m
Text.Combine({"Seattle", null, "WA"}, ", ")
```

**Output**

`"Seattle, WA"`

## Example 4

**Usage**

Combine the first name, middle initial (if present), and last name into the individual’s full name.

```powerquery-m
let
    Source = Table.FromRecords({
        [First Name = "Doug", Middle Initial = "J", Last Name = "Elis"],
        [First Name = "Anna", Middle Initial = "M", Last Name = "Jorayew"],
        [First Name = "Rada", Middle Initial = null, Last Name = "Mihaylova"]
    }),
    FullName = Table.AddColumn(Source, "Full Name", each Text.Combine({[First Name], [Middle Initial], [Last Name]}, " "))
in
    FullName
```

**Output**

```powerquery-m
Table.FromRecords({
    [First Name = "Doug", Middle Initial = "J", Last Name = "Elis", Full Name = "Doug J Elis"],
    [First Name = "Anna", Middle Initial = "M", Last Name = "Jorayew", Full Name = "Anna M Jorayew"],
    [First Name = "Rada", Middle Initial = null, Last Name = "Mihaylova", Full Name = "Rada Mihaylova"]
})
```
