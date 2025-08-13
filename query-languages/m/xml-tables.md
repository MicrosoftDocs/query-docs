---
description: "Learn more about: Xml.Tables"
title: "Xml.Tables"
ms.subservice: m-source
---
# Xml.Tables

## Syntax

<pre>
Xml.Tables(
    <b>contents</b> as any,
    optional <b>options</b> as nullable record,
    optional <b>encoding</b> as nullable number
) as table
</pre>

## About

Returns the contents of the XML document as a nested collection of flattened tables.

## Example 1

Retrieve the contents of a local XML file.

**Usage**

```powerquery-m
Xml.Tables(File.Contents("C:\invoices.xml"))
```

**Output**

`table`
