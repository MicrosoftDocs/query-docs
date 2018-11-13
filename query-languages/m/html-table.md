---
title: "Html.Table | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Html.Table

  
## About  
Returns a table containing the results of running the specified CSS selectors against the provided `html`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields:

- `RowSelector`  
  
## Syntax

<pre>
Html.Table(**html** as any, **columnNameSelectorPairs** as list, optional **options** as nullable record) as table
</pre>
  
## Example 1

Returns a table from a sample html text value.

```powerquery-m
Html.Table("<div class=""name"">Jo</div><span>Manager</span>", {{"Name", ".name"}, {"Title", "span"}}, [RowSelector=".name"])
```

<table> <tr> <th>Name</th> <th>Title</th> </tr> <tr> <td>Jo</td> <td>Manager</td> </tr> </table>

## Example 2

Extracts all the hrefs from a sample html text value.

```powerquery-m
Html.Table("<a href=""/test.html"">Test</a>", {{"Link", "a", each [Attributes][href]}})
```

<table> <tr> <th>Link</th> </tr> <tr> <td>/test.html</td> </tr> </table>