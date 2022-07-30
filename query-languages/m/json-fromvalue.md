---
description: "Learn more about: Json.FromValue"
title: "Json.FromValue"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Json.FromValue

## Syntax

<pre>
Json.FromValue(<b>value</b> as any, optional <b>encoding</b> as nullable number) as binary  
</pre>
  
## About

Produces a JSON representation of a given value `value` with a text encoding specified by `encoding`. If `encoding` is omitted, UTF8 is used. Values are represented as follows:

* Null, text and logical values are represented as the corresponding JSON types
* Numbers are represented as numbers in JSON, except that `#infinity`, `-#infinity` and `#nan` are converted to null
* Lists are represented as JSON arrays
* Records are represnted as JSON objects
* Tables are represented as an array of objects
* Dates, times, datetimes, datetimezones and durations are represented as ISO-8601 text
* Binary values are represented as base-64 encoded text
* Types and functions produce an error

## Example 1

Convert a complex value to JSON.

**Usage**

```powerquery-m
Text.FromBinary(Json.FromValue([A = {1, true, "3"}, B = #date(2012, 3, 25)]))
```

**Output**

`"{""A"":[1,true,""3""],""B"":""2012-03-25""}"`
