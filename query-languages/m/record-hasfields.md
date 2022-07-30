---
description: "Learn more about: Record.HasFields"
title: "Record.HasFields"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Record.HasFields

## Syntax

<pre>
Record.HasFields(<b>record</b> as record, <b>fields</b> as any) as logical 
</pre>
  
## About

Indicates whether the record `record` has the fields specified in `fields`, by returning a logical value (true or false). Multiple field values can be specified using a list.

## Example 1

Check if the record has the field "CustomerID".

**Usage**

```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

**Output**

`true`

## Example 2

Check if the record has the field "CustomerID" and "Address".

**Usage**

```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"], {"CustomerID", "Address"})
```

**Output**

`false`
