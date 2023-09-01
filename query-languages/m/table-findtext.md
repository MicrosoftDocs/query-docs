---
description: "Learn more about: Table.FindText"
title: "Table.FindText"
---
# Table.FindText

## Syntax

<pre>
Table.FindText(<b>table</b> as table, <b>text</b> as text) as table
</pre>
  
## About

Returns the rows in the table `table` that contain the text `text`. If the text is not found, an empty table is returned.

## Example 1

Find the rows in the table that contain "Bob".

**Usage**

```powerquery-m
Table.FindText(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Bob"
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`
