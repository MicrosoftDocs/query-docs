---
description: "Learn more about: Quick tour of the Power Query M formula language"
title: "Quick tour"
ms.date: 12/22/2023
ms.custom: nonautomated-date, intro-internal
ms.topic: conceptual
---
# Quick tour of the Power Query M formula language

This quick tour describes creating Power Query M formula language queries.

> [!NOTE]
> M is a case-sensitive language.

## Create a query with the Power Query editor

To create an advanced query, you use the [Power Query advanced editor](/power-query/power-query-ui#the-advanced-editor). A mashup query is composed of variables, expressions, and values encapsulated by a `let` expression. A variable can contain spaces by using the # identifier with the name in quotes as in `#"Variable name"`.

A `let` expression follows this structure:

```powerquery-m
let
   Variablename = expression,
   #"Variable name" = expression2
in
   Variablename
```  

To create an M query in the advanced editor, you follow this basic process:

1. Create a series of query formula steps that start with the `let` statement. Each step is defined by a step variable name. An M _variable_ can include spaces by using the # character as `#"Step Name"`. A formula step can be a custom formula. Note that the Power Query formula language is case sensitive.

2. Each query formula step builds upon a previous step by referring to a step by its variable name.

3. Output a query formula step using the `in` statement. Generally, the last query step is used as the in final data set result.

To learn more about expressions and values, go to [Expressions, values, and let expression](expressions-values-and-let-expression.md).

## Simple Power Query M formula steps

Let's assume you created the following transform in the Power Query editor to convert product names to the appropriate case, in this instance, to all initial capitalization.

:::image type="content" source="media/mstep1.png" alt-text="Screenshot of the Power Query editor showing the results of converting the Item column entries to initial capitalization.":::

To begin with, you have a table that looks like this:

|:::no-loc text="OrderID":::|:::no-loc text="CustomerID":::|:::no-loc text="Item":::|:::no-loc text="Price":::|
|-----------|--------------|--------|---------|
|1|1|:::no-loc text="fishing rod":::|100|
|2|1|:::no-loc text="1 lb. worms":::|5|
|3|2|:::no-loc text="fishing net":::|25|

And, you want to capitalize the first letter in each word in the Item column to produce the following table:

|:::no-loc text="OrderID":::|:::no-loc text="CustomerID":::|:::no-loc text="Item":::|:::no-loc text="Price":::|
|-----------|--------------|--------|---------|
|1|1|:::no-loc text="Fishing Rod":::|100|
|2|1|:::no-loc text="1 Lb. Worms":::|5|
|3|2|:::no-loc text="Fishing Net":::|25|

The M formula steps to project the original table into the results table look like this in the Power Query advanced editor:

:::image type="content" source="media/madvancededitor.png" alt-text="Screenshot of the Power Query advanced editor with all of the M formula steps to produce the table and capitalize initial letters.":::

Here's the code you can paste into the Power Query advanced editor:

```powerquery-m
let Orders = Table.FromRecords({
    [OrderID = 1, CustomerID = 1, Item = "fishing rod", Price = 100.0],
    [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
    [OrderID = 3, CustomerID = 2, Item = "fishing net", Price = 25.0]}),
    #"Capitalized Each Word" = Table.TransformColumns(Orders, {"Item", Text.Proper})
in
    #"Capitalized Each Word"
```

Let’s review each formula step.

1. **Orders**: Create a table with data for Orders.

2. **#"Capitalized Each Word"**: To capitalize each word, you use [Table.TransformColumns](table-transformcolumns.md).

3. **in #"Capitalized Each Word"**: Output the table with the first letter of each word capitalized.  
  
## Related content

* [Expressions, values, and let expression](expressions-values-and-let-expression.md)
* [Operators](operators.md)
* [Type conversion](type-conversion.md)
