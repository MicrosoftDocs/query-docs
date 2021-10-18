---
description: "Learn more about: Type.TableRow"
title: "Type.TableRow | Microsoft Docs"
ms.date: 10/18/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.TableRow

## Syntax

<pre>
Type.TableRow(<b>table</b> as type) as type 
</pre>
  
## About

Returns the row type of the specified table type. The result will always be a record type.

## Example 1

Return the row type information for a simple table.

```powerquery-m
let
    tableRowType = Type.TableRow(Value.Type(#table({"Column1"}, {})))
in
    Type.RecordFields(tableRowType)
```

`[Column1 = [Type = type any, Optional = false]]`
