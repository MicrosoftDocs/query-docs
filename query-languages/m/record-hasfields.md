---
title: "Record.HasFields | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

`true`

## Example 2
Check if the record has the field "CustomerID" and "Address".

```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"], {"CustomerID", "Address"})
```

`false`
