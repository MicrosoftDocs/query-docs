---
description: "Learn more about: Table.ToList"
title: "Table.ToList"
ms.date: 5/3/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ToList

## Syntax

<pre> 
Table.ToList(<b>table</b> as table, optional <b>combiner</b> as nullable function) as list
</pre>
  
## About

Converts a table into a list by applying the specified combining function to each row of values in the table.

## Example 1

Combine the text of each row with a comma.

**Usage**

```powerquery-m
Table.ToList(
    Table.FromRows({
        {Number.ToText(1), "Bob", "123-4567"},
        {Number.ToText(2), "Jim", "987-6543"},
        {Number.ToText(3), "Paul", "543-7890"}
    }),
    Combiner.CombineTextByDelimiter(",")
)
```

**Output**

`{"1,Bob,123-4567", "2,Jim,987-6543", "3,Paul,543-7890"}`
