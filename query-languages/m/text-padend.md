---
description: "Learn more about: Text.PadEnd"
title: "Text.PadEnd"
ms.date: 3/14/2022
---
# Text.PadEnd

## Syntax

<pre>
Text.PadEnd(<b>text</b> as nullable text, <b>count</b> as number, optional <b>character</b> as nullable text) as nullable text
</pre>
  
## About

Returns a `text` value padded to length `count` by inserting spaces at the end of the text value `text`. An optional character `character` can be used to specify the character used for padding. The default pad character is a space.

## Example 1

Pad the end of a text value so it is 10 characters long.

**Usage**

```powerquery-m
Text.PadEnd("Name", 10)
```

**Output**

<pre>"Name      "</pre>

## Example 2

Pad the end of a text value with "|" so it is 10 characters long.

**Usage**

```powerquery-m
Text.PadEnd("Name", 10, "|")
```

**Output**

<pre>"Name||||||"</pre>
