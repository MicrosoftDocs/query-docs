---
description: "Learn more about: INFO.ANNOTATIONS"
title: "INFO.ANNOTATIONS function (DAX)"
author: DataZoeMS
---
# INFO.VIEW.ANNOTATIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column in the semantic model, such as name, description, and format string. This information helps you understand the model and to self-document the model when used in calculated tables. 

## Syntax

```dax
INFO.ANNOTATIONS([<Restriction name>, <Restriction value>], ...)
```

## Parameters

Parameters are optional for this DAX function. When parameters are used, both must be given. More than one pair of parameters is allowed.

| Term | Definition |
|---|---|
| Restriction Name | Name of the restriction used to filter the results. |
| Restriction Value | Value used to filter the results of the restriction. |

## Restrictions

Typically, all columns of the DAX function results can be used as a restriction. Addtional restrictions may also be allowed.

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| [ID] | The unique ID for each column in this semantic model as an integer. |
| [Name] | The name of each column in this semantic model as a string. |
| [Table] | The table of each column in this semantic model as a string. |
| [DataType] | The data type of each column in this semantic model as a string. |
| [DataCategory] | The data category of each column in this semantic model as a string. |
| [Description] | The description of each column in this semantic model as a string. |
| [IsHidden] | The hidden state of each column in this semantic model as True or False. |
| [IsUnique] | The is unique of each column in this semantic model as True of False. |
| [IsKey] | The is key of each column in this semantic model as True or False. |
| [IsNullable] | The is nullable of each column in this semantic model as True or False. |
| [Alignment] | The alignment of each column in this semantic model as a string. |
| [SummarizeBy] | The summarize by of each column in this semantic model as a string. |
| [ColumnStorage] | The column storage of each column in this semantic model as a string combination of name and ID. |
| [Type] | The type of each column in this semantic model as a string. |
| [SourceColumn] | The source column of each column in this semantic model as a string. |
| [Expression] | The DAX formula of calculated columns. |
| [FormatString] | The format string of each column in this semantic model as a string. |
| [IsAvailableInMDX] | The is available in MDX of each column in this semantic model as True or False. Analyze in Excel pivot tables will only show columns set to True. |
| [SortByColumn] | The sort by column of each column in this semantic model as a string. Shows as blank when sorting by itself.  |
| [GroupingBehavior] | The grouping behavior of each column in this semantic model as a string. |
| [SourceProviderType] | The source provider type of each column in this semantic model as a string. |
| [DisplayFolder] | The display folder of each column in this semantic model as a string. Nested folders shown with / and multiple folders separated by ;. |
| [AlternateOf] | The alternate of property of each column in this semantic model as a string.  |
| [LineageTag] | The lineage tag of each column in this semantic model as a string. |

## Enumerations

Columns returned in this INFO function give the ID of an enumeration, or lookup table. Here are the values for each enumeration in this DAX function.

## Remarks

Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in DAX queries, and can't be used in calculations.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.VIEW.COLUMNS()
```

This DAX query returns a table with all of the columns of this DAX function.

## Example 2 - DAX query with joins to other INFO functions

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
EVALUATE
  // Select specific columns from the filtered result
  SELECTCOLUMNS(
    // Filter columns from the INFO.VIEW.COLUMNS() table
    FILTER(
      INFO.VIEW.COLUMNS(),
      // Exclude rows where DataCategory is "RowNumber" and Table is "xTables"
      [DataCategory] <> "RowNumber" && [Table] <> "xTables"
    ),
    // Show only these selected columns with new names where specified
    [Table],
    "Column", [Name],
    [Description],
    "DAX formula", [Expression],
    [DataCategory],
    [DataType],
    [IsHidden]
  )
  // Order the result by Table and then by Column
  ORDER BY
    [Table], [Column]
```

This DAX query returns a table with only the specified columns and rows meeting the filter condition with a DAX formula.

:::image type="content" source="media/info-view-columns-function-dax/dax-query-example-2.png" alt-text="Screenshot showing the output of INFO.VIEW.COLUMNS() with selected columns in DAX query view." lightbox="media/info-view-columns-function-dax/dax-query-example-2.png":::
