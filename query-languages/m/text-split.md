---
description: "Learn more about: Text.Split"
title: "Text.Split"
ms.subservice: m-source
ms.topic: reference
---
# Text.Split

## Syntax

<pre>
Text.Split(<b>text</b> as text, <b>separator</b> as text) as list
</pre>
  
## About

Returns a list of text values resulting from the splitting of a text value based on the specified delimiter.

* `text`: The text value to split.
* `separator`: The delimiter used to split the text. The delimiter can be either a single character or a sequence of characters. If a sequence of characters is used, the text is split only at instances where the exact sequence occurs.

## Example 1

Create a list from the "|" delimited text value "Name|Address|PhoneNumber".

**Usage**

```powerquery-m
Text.Split("Name|Address|PhoneNumber", "|")
```

**Output**

```powerquery-m
{
    "Name",
    "Address",
    "PhoneNumber"
}
```

## Example 2

Create a list from the text value using a sequence of characters.

**Usage**

```powerquery-m
Text.Split("Name, the Customer, the Purchase Date", ", the ")
```

**Output**

```powerquery-m
{
    Name,
    Customer,
    Purchase Date
}
```
