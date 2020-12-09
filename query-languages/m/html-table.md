---
title: "Html.Table | Microsoft Docs"
ms.date: 06/15/2020
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Html.Table

## Syntax

<pre>
Html.Table(<b>html</b> as any, <b>columnNameSelectorPairs</b> as list, optional <b>options</b> as nullable record) as table
</pre>
  
## About 
Returns a table containing the results of running the specified CSS selectors against the provided `html`. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields: 

* `RowSelector` 

## Example 1
Returns a table from a sample html text value.

```
Html.Table("<div class=""name"">Jo</div><span>Manager</span>", {{"Name", ".name"}, {"Title", "span"}}, [RowSelector=".name"])\
```

```
#table({"Name", "Title"}, {{"Jo", "Manager"}})
```

## Example 2
Extracts all the hrefs from a sample html text value.

```
Html.Table("<a href=""/test.html"">Test</a>", {{"Link", "a", each [Attributes][href]}})
```

```
#table({"Link"}, {{"/test.html"}})
```
