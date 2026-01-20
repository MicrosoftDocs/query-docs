---
description: "Learn more about: List.Select"
title: "List.Select"
ms.subservice: m-source
ms.topic: reference
---
# List.Select

## Syntax

<pre>
List.Select(<b>list</b> as list, <b>selection</b> as function) as list
</pre>
  
## About

Returns the values from the specified list that match the selection condition.

* `list`: The list to examine.
* `selection`: The function that determines the values to select.

## Example 1

Find the values in the list {1, -3, 4, 9, -2} that are greater than 0.

**Usage**

```powerquery-m
List.Select({1, -3, 4, 9, -2}, each _ > 0)
```

**Output**

`{1, 4, 9}`

## Example 2

Select dates from the list that fall on Saturday or Sunday.

**Usage**

```powerquery-m
let
    dates = {
        #date(2025, 10, 20),  // Monday
        #date(2025, 10, 21),  // Tuesday
        #date(2025, 10, 25),  // Saturday
        #date(2025, 10, 26),  // Sunday
        #date(2025, 10, 27)   // Monday
    },
    weekendDates = List.Select(
        dates,
        each Date.DayOfWeek(_, Day.Monday) >= 5
    )
in
    weekendDates
```

**Output**

```powerquery-m
{
    #date(2025, 10, 25),
    #date(2025, 10, 26)
}
```

## Example 3

Display a table of active customers with purchase totals over $100.

**Usage**

```powerquery-m
let
    customers = {
        [Name = "Alice", Status = "Active", Purchases = 150],
        [Name = "Bob", Status = "Inactive", Purchases = 200],
        [Name = "Carol", Status = "Active", Purchases = 90],
        [Name = "Dave", Status = "Active", Purchases = 120]
    },
    highValueActiveCustomers = List.Select(
        customers,
        each [Status] = "Active" and [Purchases] > 100
    ),
    resultTable = Table.FromRecords(
        highValueActiveCustomers,
        type table [Name = text, Status = text, Purchases = number]
    )
in
    resultTable
```

**Output**

```powerquery-m
#table(type table[Name = text, Status = text, Purchases = number],
{
    {"Alice", "Active", 150},
    {"Dave", "Active", 120}
})
```
