---
description: "Learn more about: Text.PadStart"
title: "Text.PadStart"
ms.date: 3/14/2022
---
# Text.PadStart

## Syntax

<pre>
Text.PadStart(<b>text</b> as nullable text, <b>count</b> as number, optional <b>character</b> as nullable text) as nullable text
</pre>
  
## About

Returns a `text` value padded to length `count` by inserting spaces at the start of the text value `text`. An optional character `character` can be used to specify the character used for padding. The default pad character is a space.

## Example 1

Pad the start of a text value so it is 10 characters long.

**Usage**

```powerquery-m
Text.PadStart("Name", 10)
```

**Output**

<pre>"      Name"</pre>

## Example 2

Pad the start of a text value with "|" so it is 10 characters long.

**Usage**

```powerquery-m
Text.PadStart("Name", 10, "|")
```

**Output**

<pre>"||||||Name"</pre>
