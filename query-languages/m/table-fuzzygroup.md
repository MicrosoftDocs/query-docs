---
title: "Table.FuzzyGroup | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.FuzzyGroup
  
## Syntax

<pre>
Table.FuzzyGroup(<b>table</b> as table, <b>key</b> as any, <b>aggregatedColumns</b> as list, optional <b>options</b> as nullable record) as table
</pre>
  

## About

Groups the rows of `table` by fuzzily matching values in the specified column, `key`, for each row. For each group, a record is constructed containing the key columns (and their values) along with any aggregated columns specified by `aggregatedColumns`. This function cannot guarantee to return a fixed order of rows.

An optional set of `options` may be included to specify how to compare the key columns. Options include:

* `Culture`
* `IgnoreCase`
* `IgnoreSpace`
* `Threshold`
* `TransformationTable`

The following table provides more details about the advanced options. 

|Advanced Option |Default |Allowed |Description |
| --- | --- | --- | --- |
|Culture |Culture neutral |A valid culture name |The Culture option allows matching records based on culture-specific rules. <br/> For example, a Culture option of 'ja-JP' matches records based on the Japanese language. |
|IgnoreCase |true |true or false |The IgnoreCase option allows grouping of keys irrespective of the case of the text. <br/> For example, 'Grapes' (sentence case) is grouped with 'grapes' (lower case) if the IgnoreCase option is set to true. |
|IgnoreSpace |true |true or false |The IgnoreSpace option allows combining text parts in order to find matches. <br/> For example, 'Micro soft' is grouped with 'Microsoft' if the IgnoreSpace option is set to true. |
|Threshold |0.80 |Between 0.00 and 1.00 |The similarity Threshold option provides the ability to match records above a given similarity score. A threshold of 1.00 is the same as specifying an exact match criteria. <br/> For example, 'Grapes' and 'Graes' (missing 'p') are grouped only if the thresold is set to less than 0.90. |
|TransformationTable | |A valid table with at least 2 columns named 'From' and 'To'. |The TransformationTable option allows matching records based on custom value mappings. <br/> For example, 'Grapes' are matched with 'Raisins' if a transformation table is provided with the 'From' column containing 'Grapes' and the 'To' column containing 'Raisins'. Note that the transformation will be applied to all occurrences of the text in the transformation table. For example, with the above transformation table 'Grapes are sweet' will also be matched with 'Raisins are sweet'. |
| | | | | 

## Example

Group the table adding an aggregate column [Count] that contains the number of employees in each location (`each Table.RowCount(_)`).

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

|Location |Count |
| --- | --- |
|Seattle |4 |
|Vancouver |3 |
| | |

