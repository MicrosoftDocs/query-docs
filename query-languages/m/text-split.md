---
description: "Learn more about: Text.Split"
title: "Text.Split"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Split

## Syntax

<pre>
Text.Split(<b>text</b> as text, <b>separator</b> as text) as list
</pre>
  
## About

Returns a list of text values resulting from the splitting a text value `text` based on the specified delimiter, `separator`.

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
