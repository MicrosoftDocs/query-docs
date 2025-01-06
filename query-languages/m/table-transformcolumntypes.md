---
description: "Learn more about: Table.TransformColumnTypes"
title: "Table.TransformColumnTypes"
ms.subservice: m-source
---
# Table.TransformColumnTypes

## Syntax

<pre>
Table.TransformColumnTypes(<b>table</b> as table, <b>typeTransformations</b> as list, optional <b>culture</b> as nullable text) as table
</pre>
  
## About

Returns a table from the input `table` by applying the transform operation to the columns specified in the parameter `typeTransformations` (where format is {column name, type name}), using the specified culture in the optional parameter `culture` (for example, "en-US"). If the column doesn't exist, an exception is thrown.

- [Type](/powerquery-m/type-conversion) - Power Query M uses types to classify values to have a more structured data set. The article linked describes the most commonly used types.
- [Culture](/powerquery-m/how-culture-affects-text-formatting) - The default culture is set to the system locale ([Windows](/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c), MacOS) of a particular document where your queries are first authored. 

## Example 1

Transform the number values in column [a] to text values from the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

**Usage**

```powerquery-m
Table.TransformColumnTypes(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4]
    }),
    {"a", type text},
    "en-US"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = "1", b = 2],
    [a = "3", b = 4]
})
```

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
