---
title: "Understanding ORDERBY, PARTITIONBY, and MATCHBY functions in DAX"
description: Best practices for using ORDERBY, PARTITIONBY, and MATCHBY functions.
author: jeroenterheerdt
ms.topic: conceptual
ms.date: 07/07/2023
---

# Understanding ORDERBY, PARTITIONBY, and MATCHBY functions

The [ORDERBY](../orderby-function-dax.md), [PARTITIONBY](../partitionby-function-dax.md), and [MATCHBY](../matchby-function-dax.md) functions in DAX are special functions that can only be used along with DAX Window functions: [INDEX](../index-function-dax.md), [OFFSET](../offset-function-dax.md), [WINDOW](../window-function-dax.md), [RANK](../rank-function-dax.md), [ROWNUMBER](../rownumber-function-dax.md).

Understanding ORDERBY, PARTITIONBY, and MATCHBY is critical to successfully using the Window functions. The examples provided here use OFFSET, but are similarly applicable to the other Window functions.

## Scenario

Let’s start with an example that doesn't use Window functions at all. Shown below is a table that returns total sales, per color, per calendar year. There are multiple ways to define this table, but since we're interested in understanding what happens in DAX, we'll use a calculated table. Here's the table expression:

```dax
BasicTable = 
    SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
    )

```

You'll see this calculated table expression uses [SUMMARIZECOLUMNS](../summarizecolumns-function-dax.md) to calculate the SUM of the SalesAmount column in the FactInternetSales table, by the Color column from the DimProduct table, and the CalendarYear column from the DimDate table. Here's The result:

| Color    | CalendarYear | CurrentYearSales |
|----------|--------------|------------------|
| "Black"  | 2017         | 393885           |
| "Black"  | 2018         | 1818835          |
| "Black"  | 2019         | 3981638          |
| "Black"  | 2020         | 2644054          |
| "Blue"   | 2019         | 994448           |
| "Blue"   | 2020         | 1284648          |
| "Multi"  | 2019         | 48622            |
| "Multi"  | 2020         | 57849            |
| "NA"     | 2019         | 207822           |
| "NA"     | 2020         | 227295           |
| "Red"    | 2017         | 2961198          |
| "Red"    | 2018         | 3686935          |
| "Red"    | 2019         | 900175           |
| "Red"    | 2020         | 176022           |
| "Silver" | 2017         | 326399           |
| "Silver" | 2018         | 750026           |
| "Silver" | 2019         | 2165176          |
| "Silver" | 2020         | 1871788          |
| "White"  | 2019         | 2517             |
| "White"  | 2020         | 2589             |
| "Yellow" | 2018         | 163071           |
| "Yellow" | 2019         | 2072083          |
| "Yellow" | 2020         | 2621602          |

Now, let’s imagine we're trying to solve the business question of calculating the difference in sales, year-over-year for each color. Effectively, we need a way to find sales for the same color in the previous year and subtract that from the sales in the current year, in context. For example, for the combination [Red, 2019] we're looking for sales for [Red, 2018]. Once we have that, we can then subtract it from the current sales and return the required value.

### Using OFFSET

OFFSET is perfect for the typical *compare with previous* types of calculations required to answer the business question described above, as it allows us to do a relative movement. Our first attempt might be:

```dax
1stAttempt = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "PreviousColorSales",
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation
            ),
            [CurrentYearSales]
        )
    )

```

A lot is happening with this expression. We used [ADDCOLUMNS](../addcolumns-function-dax.md) to expand the table from before with a column called PreviousColorSales. The contents of that column are set to the CurrentYearSales, which is SUM(FactInternetSales[SalesAmount]), for the previous Color (retrieved using OFFSET).

The result is:

| Color    | CalendarYear | CurrentYearSales | PreviousColorSales |
|----------|--------------|------------------|--------------------|
| "Black"  | 2017         | 393885           |                    |
| "Black"  | 2018         | 1818835          | 393885             |
| "Black"  | 2019         | 3981638          | 1818835            |
| "Black"  | 2020         | 2644054          | 3981638            |
| "Blue"   | 2019         | 994448           | 2644054            |
| "Blue"   | 2020         | 1284648          | 994448             |
| "Multi"  | 2019         | 48622            | 1284648            |
| "Multi"  | 2020         | 57849            | 48622              |
| "NA"     | 2019         | 207822           | 57849              |
| "NA"     | 2020         | 227295           | 207822             |
| "Red"    | 2017         | 2961198          | 227295             |
| "Red"    | 2018         | 3686935          | 2961198            |
| "Red"    | 2019         | 900175           | 3686935            |
| "Red"    | 2020         | 176022           | 900175             |
| "Silver" | 2017         | 326399           | 176022             |
| "Silver" | 2018         | 750026           | 326399             |
| "Silver" | 2019         | 2165176          | 750026             |
| "Silver" | 2020         | 1871788          | 2165176            |
| "White"  | 2019         | 2517             | 1871788            |
| "White"  | 2020         | 2589             | 2517               |
| "Yellow" | 2018         | 163071           | 2589               |
| "Yellow" | 2019         | 2072083          | 163071             |
| "Yellow" | 2020         | 2621602          | 2072083            |

This is one step closer to our goal, but if we look closely it doesn't match exactly what we're after. For example, for [Silver, 2017] the PreviousColorSales is set to [Red, 2020].

### Adding ORDERBY

That definition above is equivalent to:

```dax
1stAttemptWithORDERBY = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "PreviousColorSales",
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([Color], ASC, [CalendarYear], ASC, [CurrentYearSales], ASC)      
            ),
            [CurrentYearSales]
        )
    )

```

In this case, the call to OFFSET uses ORDERBY to order the table by Color and CalendarYear in ascending order, which determines what is considered the previous row that's returned.

The reason these two results are equivalent is because ORDERBY automatically contains all columns from the relation that aren't in PARTITIONBY. Since PARTITIONBY wasn't specified, ORDERBY is set to Color, CalendarYear, and CurrentYearSales. However, since the Color and CalendarYear pairs in the relation are unique, adding CurrentYearSales doesn't change the result. In fact, even if we were to only specify Color in ORDERBY, the results are the same since CalendarYear would be automatically added. This is because the function will add as many columns as needed to ORDERBY in order to ensure each row can be uniquely identified by the ORDERBY and PARTITIONBY columns:

```dax
1stAttemptWithORDERBY = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS(
        vRelation,
        "PreviousColorSales",
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([Color])
            ),
            [CurrentYearSales]
        )
    )

```

### Adding PARTITIONBY

Now, to *almost* get the result we're after we can use PARTITIONBY, as shown in the following calculated table expression:

```dax
UsingPARTITIONBY = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "PreviousColorSales",
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([CalendarYear]), 
                PARTITIONBY ([Color])
            ),
            [CurrentYearSales]
        )
    )

```

Notice that specifying ORDERBY is optional here because ORDERBY automatically contains all the columns from the relation that aren't specified in PARTITIONBY. So, the following expression returns the same results because ORDERBY is set to CalendarYear and CurrentYearSales automatically:

```dax
UsingPARTITIONBYWithoutORDERBY = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "PreviousColorSales",
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                PARTITIONBY ([Color])
            ),
            [CurrentYearSales]
        )
    )


```

> [!NOTE]
> While ORDERBY is set to CalendarYear and CurrentYearSales automatically, no guarantee is given as to what order in which they'll be added. If CurrentYearSales is added before CalendarYear, the resulting order isn't inline with what's expected. **Be explicit when specifying ORDERBY and PARTITIONBY to avoid confusion and unexpected results**.  

Both expressions return the result we're after:

| Color    | CalendarYear | CurrentYearSales | PreviousYearSalesForSameColor |
|----------|--------------|------------------|-------------------------------|
| "Black"  | 2017         | 393885           |                               |
| "Black"  | 2018         | 1818835          | 393885                        |
| "Black"  | 2019         | 3981638          | 1818835                       |
| "Black"  | 2020         | 2644054          | 3981638                       |
| "Blue"   | 2019         | 994448           |                               |
| "Blue"   | 2020         | 1284648          | 994448                        |
| "Multi"  | 2019         | 48622            |                               |
| "Multi"  | 2020         | 57849            | 48622                         |
| "NA"     | 2019         | 207822           |                               |
| "NA"     | 2020         | 227295           | 207822                        |
| "Red"    | 2017         | 2961198          |                               |
| "Red"    | 2018         | 3686935          | 2961198                       |
| "Red"    | 2019         | 900175           | 3686935                       |
| "Red"    | 2020         | 176022           | 900175                        |
| "Silver" | 2017         | 326399           |                               |
| "Silver" | 2018         | 750026           | 326399                        |
| "Silver" | 2019         | 2165176          | 750026                        |
| "Silver" | 2020         | 1871788          | 2165176                       |
| "White"  | 2019         | 2517             |                               |
| "White"  | 2020         | 2589             | 2517                          |
| "Yellow" | 2018         | 163071           |                               |
| "Yellow" | 2019         | 2072083          | 163071                        |
| "Yellow" | 2020         | 2621602          | 2072083                       |

As you see in this table, the PreviousYearSalesForSameColor column shows the sales for the previous year for the same color. For [Red, 2020], it returns the sales for [Red, 2019], and so on. If there's no previous year, for example in the case of [Red, 2017], no value is returned.

You can think of PARTITIONBY as a way to divide the table into parts in which to execute the OFFSET calculation. In the example above, the table is divided into as many parts as there are colors, one for each color. Then, within each part, the OFFSET is calculated, sorted by CalendarYear.

Visually, what's happening is this:

:::image type="content" source="media/dax-understand-orderby/offset-by-calendar-year.png" border="false" alt-text="Table showing OFFSET by Calendar Year":::

First, the call to PARTITIONBY results in the table getting divided into parts, one for each Color. This is represented by the light blue boxes in the table image. Next, ORDERBY makes sure that each part is sorted by CalendarYear (represented by the orange arrows). Finally, within each sorted part, for each row, OFFSET finds the row above it and returns that value in the PreviousYearSalesForSameColor column. Since for every first row in each part there is no previous row in that same part, the result in that row for the PreviousYearSalesForSameColor column is empty.

To achieve the final result, we simply have to subtract CurrentYearSales from the previous year sales for the same color returned by the call to OFFSET. Since we're not interested in showing the previous year sales for the same color, but only in the current year sales and the year over year difference. Here's the final calculated table expression:

```dax
FinalResult = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "YoYSalesForSameColor",
        [CurrentYearSales] -
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([CalendarYear]),
                PARTITIONBY ([Color])
            ),
            [CurrentYearSales]
        )
    )

```

And here's the result of that expression:

| Color    | CalendarYear | CurrentYearSales | YoYSalesForSameColor |
|----------|--------------|------------------|----------------------|
| "Black"  | 2017         | 393885           | 393885               |
| "Black"  | 2018         | 1818835          | 1424950              |
| "Black"  | 2019         | 3981638          | 2162803              |
| "Black"  | 2020         | 2644054          | -1337584             |
| "Blue"   | 2019         | 994448           | 994448               |
| "Blue"   | 2020         | 1284648          | 290200               |
| "Multi"  | 2019         | 48622            | 48622                |
| "Multi"  | 2020         | 57849            | 9227                 |
| "NA"     | 2019         | 207822           | 207822               |
| "NA"     | 2020         | 227295           | 19473                |
| "Red"    | 2017         | 2961198          | 2961198              |
| "Red"    | 2018         | 3686935          | 725737               |
| "Red"    | 2019         | 900175           | -2786760             |
| "Red"    | 2020         | 176022           | -724153              |
| "Silver" | 2017         | 326399           | 326399               |
| "Silver" | 2018         | 750026           | 423627               |
| "Silver" | 2019         | 2165176          | 1415150              |
| "Silver" | 2020         | 1871788          | -293388              |
| "White"  | 2019         | 2517             | 2517                 |
| "White"  | 2020         | 2589             | 72                   |
| "Yellow" | 2018         | 163071           | 163071               |
| "Yellow" | 2019         | 2072083          | 1909012              |
| "Yellow" | 2020         | 2621602          | 549519               |

### Using MATCHBY

You might have noticed we didn't specify MATCHBY at all. In this case, it isn't necessary. The columns in ORDERBY and PARTITIONBY (for as far as they were specified in the examples above) are sufficient to uniquely identify each row. Since we didn't specify MATCHBY, the columns specified in ORDERBY and PARTITIONBY are used to uniquely identify each row so they can be compared to enable OFFSET to give a meaningful result. If the columns in ORDERBY and PARTITIONBY can’t uniquely identify each row, additional columns can be added to the ORDERBY clause if those extra columns allow each row to be uniquely identified. If that's not possible, an error is returned. In this last case, specifying MATCHBY may help to resolve the error.

If MATCHBY is specified, the columns in MATCHBY and PARTITIONBY are used to uniquely identify each row. If that's not possible, an error is returned. Even if MATCHBY isn't required, consider explicitly specifying MATCHBY to avoid any confusion.

Continuing from the examples above, here's the last expression:

```dax
FinalResult = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "YoYSalesForSameColor",
        [CurrentYearSales] -
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([CalendarYear]),
                PARTITIONBY ([Color])
            ),
            [CurrentYearSales]
        )
    )

```

If we want to be explicit about how rows should be uniquely identified, we can specify MATCHBY as shown in the following equivalent expression:

```dax
FinalResultWithExplicitMATCHBYOnColorAndCalendarYear = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "YoYSalesForSameColor",
        [CurrentYearSales] -
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([CalendarYear]),
                PARTITIONBY ([Color]),
                MATCHBY ([Color], [CalendarYear])
            ),
            [CurrentYearSales]
        )
    )

```

Since MATCHBY is specified, both the columns specified in MATCHBY as well as in PARTITIONBY are used to uniquely identify rows. Since Color is specified in both MATCHBY and PARTITIONBY, the following expression is equivalent to the previous expression:

```dax
FinalResultWithExplicitMATCHBYOnCalendarYear = 
    VAR vRelation = SUMMARIZECOLUMNS ( 
        DimProduct[Color], 
        DimDate[CalendarYear], 
        "CurrentYearSales", ROUND ( SUM ( FactInternetSales[SalesAmount] ), 0 )
        )
    RETURN
    ADDCOLUMNS (
        vRelation,
        "YoYSalesForSameColor",
        [CurrentYearSales] -
        SELECTCOLUMNS (
            OFFSET (
                -1,
                vRelation,
                ORDERBY ([CalendarYear]),
                PARTITIONBY ([Color]),
                MATCHBY ([CalendarYear])
            ),
            [CurrentYearSales]
        )
    )

```

Since specifying MATCHBY isn't necessary in the examples we've looked at so far, let’s look at a slightly different example that does require MATCHBY. In this case, we have a list of order lines. Each row represents an order line for an order. An order can have multiple order lines and order line 1 appears on many orders. In addition, for each order line we have a ProductKey and a SalesAmount. A sample of the relevant columns on the table looks like this:

| SalesOrderNumber | SalesOrderLineNumber | ProductKey | SalesAmount |
|------------------|----------------------|------------|-------------|
| SO51900          | 1                    | 528        | 4.99        |
| SO51948          | 1                    | 528        | 5.99        |
| SO52043          | 1                    | 528        | 4.99        |
| SO52045          | 1                    | 528        | 4.99        |
| SO52094          | 1                    | 528        | 4.99        |
| SO52175          | 1                    | 528        | 4.99        |
| SO52190          | 1                    | 528        | 4.99        |
| SO52232          | 1                    | 528        | 4.99        |
| SO52234          | 1                    | 528        | 4.99        |
| SO52234          | 2                    | 529        | 3.99        |

Notice SalesOrderNumber and SalesOrderLineNumber are both required to uniquely identify rows.

For each order, we want to return the previous sales amount of the same product (represented by the ProductKey) ordered by the SalesAmount in descending order. The following expression won't work because there are potentially multiple rows in vRelation as it's passed into OFFSET:

```dax
ThisExpressionFailsBecauseMATCHBYIsMissing = 
    ADDCOLUMNS (
        FactInternetSales,
        "Previous Sales Amount",
            SELECTCOLUMNS (
                OFFSET (
                    -1,
                    FactInternetSales,
                    ORDERBY ( FactInternetSales[SalesAmount], DESC ),
                    PARTITIONBY ( FactInternetSales[ProductKey] )
                ),
                FactInternetSales[SalesAmount]
            )
    )

```

This expression returns an error: "OFFSET's Relation parameter may have duplicate rows, which isn't allowed."

In order to make this expression work, MATCHBY must be specified and must include all columns that uniquely define a row. MATCHBY is required here because the relation, FactInternetSales, doesn't contain any explicit keys or unique columns. However, the columns SalesOrderNumber and SalesOrderLineNumber together form a *composite key*, where their existence together is unique in the relation and can therefore uniquely identify each row. Just specifying SalesOrderNumber or SalesOrderLineNumber isn't enough as both columns contain repeating values. The following expression solves the problem:

```dax
ThisExpressionWorksBecauseOfMATCHBY = 
    ADDCOLUMNS (
        FactInternetSales,
        "Previous Sales Amount",
            SELECTCOLUMNS (
                OFFSET (
                    -1,
                    FactInternetSales,
                    ORDERBY ( FactInternetSales[SalesAmount], DESC ),
                    PARTITIONBY ( FactInternetSales[ProductKey] ),
                    MATCHBY ( FactInternetSales[SalesOrderNumber], 
                                FactInternetSales[SalesOrderLineNumber] )
                ),
                FactInternetSales[SalesAmount]
            )
    )

```

And this expression does indeed return the results we're after:

| SalesOrderNumber    | SalesOrderLineNumber | ProductKey | SalesAmount | Previous Sales Amount |
|---------------------|----------------------|------------|-------------|-----------------------|
| SO51900             | 1                    | 528        | 5.99        |                       |
| SO51948             | 1                    | 528        | 4.99        | 5.99                  |
| SO52043             | 1                    | 528        | 4.99        | 4.99                  |
| SO52045             | 1                    | 528        | 4.99        | 4.99                  |
| SO52094             | 1                    | 528        | 4.99        | 4.99                  |
| SO52175             | 1                    | 528        | 4.99        | 4.99                  |
| SO52190             | 1                    | 528        | 4.99        | 4.99                  |
| SO52232             | 1                    | 528        | 4.99        | 4.99                  |
| SO52234             | 1                    | 528        | 4.99        | 4.99                  |
| SO52234             | 2                    | 529        | 3.99        |                       |

## Related content

[ORDERBY](../orderby-function-dax.md)  
[PARTITIONBY](../partitionby-function-dax.md)  
[MATCHBY](../matchby-function-dax.md)  
[INDEX](../index-function-dax.md)  
[OFFSET](../offset-function-dax.md)  
[WINDOW](../window-function-dax.md)  
[RANK](../rank-function-dax.md)  
[ROWNUMBER](../rownumber-function-dax.md)
