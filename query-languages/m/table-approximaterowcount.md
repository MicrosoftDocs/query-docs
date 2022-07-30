---
description: "Learn more about: Table.ApproximateRowCount"
title: "Table.ApproximateRowCount | Microsoft Docs"
ms.date: 3/16/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ApproximateRowCount

## Syntax

<pre>
Table.ApproximateRowCount(<b>table</b> as table) as number
</pre>

## About

Returns the approximate number of rows in the `table`, or an error if the data source doesn't support approximation.

## Example 1

Estimate the number of distinct combinations of city and state in a large table, which can be used as a cardinality estimate for the columns. Cardinality estimates are important enough that various data sources (such as SQL Server) support this particular approximation, often using an algorithm called HyperLogLog.

**Usage**

```powerquery-m
Table.ApproximateRowCount(Table.Distinct(Table.SelectColumns(sqlTable, {"city", "state"})))
```

**Output**

`number`
