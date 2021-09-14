---
description: "Learn more about: Xml.Tables"
title: "Xml.Tables | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Xml.Tables

## Syntax

<pre>
Xml.Tables(<b>contents</b> as any, optional <b>options</b> as nullable record, optional <b>encoding</b> as nullable number) as table
</pre>

## About

Returns the contents of the XML document as a nested collection of flattened tables.

## Example 1

Retrieve the contents of a local XML file.

```powerquery-m
Xml.Tables(File.Contents("C:\invoices.xml"))
```

`
table
`
