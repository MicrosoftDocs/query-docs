---
description: "Learn more about: COMBINEVALUES"
title: "COMBINEVALUES function (DAX)"
---

# COMBINEVALUES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Joins two or more text strings into one text string. The primary purpose of this function is to support multi-column relationships in DirectQuery models. See [remarks](#remarks) for details.

## Syntax

```dax
COMBINEVALUES(<delimiter>, <expression>, <expression>[, <expression>]…)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`delimiter`|A separator to use during concatenation. Must be a constant value.|
|`expression`|A DAX expression whose value will be joined into a single text string.|

## Return value

A concatenated string.

## Remarks

- The COMBINEVALUES function assumes, but does not validate, that when the input values are different, the output strings are also different. Based on this assumption, when COMBINEVALUES is used to create calculated columns in order to build a relationship that joins multiple columns from two DirectQuery tables, an optimized join condition is generated at query time. For example, if users want to create a relationship between Table1(Column1, Column2) and Table2(Column1, Column2), they can create two calculated columns, one on each table, as:

    ```dax
    Table1[CalcColumn] = COMBINEVALUES(",", Table1[Column1], Table1[Column2])
    ```

    and

    ```dax
    Table2[CalcColumn] = COMBINEVALUES(",", Table2[Column1], Table2[Column2])
    ```

    And then create a relationship between `Table1[CalcColumn]` and `Table2[CalcColumn]`. Unlike other DAX functions and operators, which are translated literally to the corresponding SQL operators and functions, the above relationship generates a SQL join predicate as:

    ```dax
    (Table1.Column1 = Table2.Column1 OR Table1.Column1 IS NULL AND Table2.Column1 IS NULL)
    ```

    and

    ```dax
    (Table1.Column2 = Table2.Column2 OR Table1.Column2 IS NULL AND Table2.Column2 IS NULL)
    ```

- The join predicate can potentially deliver much better query performance than one that involves complex SQL operators and functions.

- The COMBINEVALUES function relies on users to choose the appropriate delimiter to ensure that unique combinations of input values produce distinct output strings but it does not validate that the assumption is true. For example, if users choose `"| "` as the delimiter, but one row in Table1 has `Table1[Column1] = "| "` and `Table2 [Column2] = " "`, while one row in Table2 has `Table2[Column1] = " "` and `Table2[Column2] = "| "`, the two concatenated outputs will be the same `"|| "`,  which seem to indicate that the two rows are a match in the join operation. The two rows are not joined together if both tables are from the same DirectQuery source although they are joined together if both tables are imported.

## Example

The following DAX query:

```dax
EVALUATE
DISTINCT (
    SELECTCOLUMNS ( Date, "Month", COMBINEVALUES ( ", ", [MonthName], [CalendarYear] ) )
)
```

Returns the following single column table:

|[Month]  |
|---------|
|January, 2020     |
|February, 2020    |
|March, 2020    |
|April, 2020     |
|May, 2020     |
|June, 2020     |
|July, 2020     |
|August, 2020     |
|September, 2020     |
|October, 2020     |
|November, 2020    |
|December, 2020     |
|January, 2021     |
|January, 2021     |
|February, 2021    |
|March, 2021    |
|April, 2021     |
|May, 2021     |
|June, 2021     |
|July, 2021     |
|August, 2021     |
|September, 2021     |
|October, 2021     |
|November, 2021    |
|December, 2021     |
