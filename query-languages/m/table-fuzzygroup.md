---
description: "Learn more about: Table.FuzzyGroup"
title: "Table.FuzzyGroup"
ms.subservice: m-source
---
# Table.FuzzyGroup
  
## Syntax

<pre>
Table.FuzzyGroup(
    <b>table</b> as table,
    <b>key</b> as any,
    <b>aggregatedColumns</b> as list,
    optional <b>options</b> as nullable record
) as table
</pre>
  
## About

Groups the rows of `table` by fuzzily matching values in the specified column, `key`, for each row. For each group, a record is constructed containing the key columns (and their values) along with any aggregated columns specified by `aggregatedColumns`. This function cannot guarantee to return a fixed order of rows.

An optional set of `options` may be included to specify how to compare the key columns. Options include:

* `Culture`: Allows grouping records based on culture-specific rules. It can be any valid culture name. For example, a Culture option of "ja-JP" groups records based on the Japanese culture. The default value is "", which groups based on the Invariant English culture.
* `IgnoreCase`: A logical (true/false) value that allows case-insensitive key grouping. For example, when true, "Grapes" is grouped with "grapes". The default value is true.
* `IgnoreSpace`: A logical (true/false) value that allows combining of text parts in order to find groups. For example, when true, "Gra pes" is grouped with "Grapes". The default value is true.
* `SimilarityColumnName`: A name for the column that shows the similarity between an input value and the representative value for that input. The default value is null, in which case a new column for similarities will not be added.
* `Threshold`: A number between 0.00 and 1.00 that specifies the similarity score at which two values will be grouped. For example, "Grapes" and "Graes" (missing the "p") are grouped together only if this option is set to less than 0.90. A threshold of 1.00 only allows exact matches. (Note that a fuzzy "exact match" might ignore differences like casing, word order, and punctuation.) The default value is 0.80.
* `TransformationTable`: A table that allows grouping records based on custom value mappings. It should contain "From" and "To" columns. For example, "Grapes" is grouped with "Raisins" if a transformation table is provided with the "From" column containing "Grapes" and the "To" column containing "Raisins". Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, "Grapes are sweet" will also be grouped with "Raisins are sweet".

## Example 1

Group the table adding an aggregate column [Count] that contains the number of employees in each location (`each Table.RowCount(_)`).

**Usage**

```powerquery-m
Table.FuzzyGroup(
    Table.FromRecords(
        {
            [EmployeeID = 1, Location = "Seattle"],
            [EmployeeID = 2, Location = "seattl"],
            [EmployeeID = 3, Location = "Vancouver"],
            [EmployeeID = 4, Location = "Seatle"],
            [EmployeeID = 5, Location = "vancover"],
            [EmployeeID = 6, Location = "Seattle"],
            [EmployeeID = 7, Location = "Vancouver"]
        },
        type table [EmployeeID = nullable number, Location = nullable text]
    ),
    "Location",
    {"Count", each Table.RowCount(_)},
    [IgnoreCase = true, IgnoreSpace = true]
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Location = "Seattle", Count = 4],
    [Location = "Vancouver", Count = 3]
})
```

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
