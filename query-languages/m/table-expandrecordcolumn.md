---
description: "Learn more about: Table.ExpandRecordColumn"
title: "Table.ExpandRecordColumn"
ms.subservice: m-source
---
# Table.ExpandRecordColumn

## Syntax

<pre>
Table.ExpandRecordColumn(<b>table</b> as table, <b>column</b> as text, <b>fieldNames</b> as list, optional <b>newColumnNames</b> as nullable list) as table
</pre>
  
## About

Given the `column` of records in the input `table`, creates a table with a column for each field in the record. Optionally, `newColumnNames` may be specified to ensure unique names for the columns in the new table.

* `table`: The original table with the record column to expand.
* `column`: The column to expand.
* `fieldNames`: The list of fields to expand into columns in the table.
* `newColumnNames`: The list of column names to give the new columns. The new column names cannot duplicate any column in the new table.

## Example 1

Expand column [a] in the table `({[a = [aa = 1, bb = 2, cc = 3], b = 2]})` into 3 columns "aa", "bb" and "cc".

**Usage**

```powerquery-m
Table.ExpandRecordColumn(
    Table.FromRecords({
        [
            a = [aa = 1, bb = 2, cc = 3],
            b = 2
        ]
    }),
    "a",
    {"aa", "bb", "cc"}
)
```

**Output**

`Table.FromRecords({[aa = 1, bb = 2, cc = 3, b = 2]})`
