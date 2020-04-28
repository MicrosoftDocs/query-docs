---
title: "Uri.BuildQueryString | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Uri.BuildQueryString

## Syntax

<pre>
Uri.BuildQueryString(<b>query</b> as record) as text
</pre>

## About
Assemble the record `query` into a URI query string, escaping characters as necessary.

## Example 
Encode a query string which contains some special characters.

```powerquery-m
Uri.BuildQueryString([a = "1", b = "+$"])
```

`"a=1&b=%2B%24"`

