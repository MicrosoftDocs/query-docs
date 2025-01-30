---
description: "Learn more about: Html.Table"
title: "Html.Table"
ms.subservice: m-source
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

**Usage**

```powerquery-m
Html.Table("<div class=""name"">Jo</div><span>Manager</span>", {{"Name", ".name"}, {"Title", "span"}}, [RowSelector=".name"])\
```

**Output**

`#table({"Name", "Title"}, {{"Jo", "Manager"}})`

## Example 2

Extracts all the hrefs from a sample html text value.

**Usage**

```powerquery-m
Html.Table("<a href=""/test.html"">Test</a>", {{"Link", "a", each [Attributes][href]}})
```

**Output**

`#table({"Link"}, {{"/test.html"}})`
