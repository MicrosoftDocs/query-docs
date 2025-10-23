---
description: "Learn more about: List.Count"
title: "List.Count"
ms.subservice: m-source
---
# List.Count

## Syntax

<pre>
List.Count(<b>list</b> as list) as number
</pre>

## About

Returns the number of items in the specified list.

* `list`: The list to examine.

## Example 1

Find the number of values in the list {1, 2, 3}.

**Usage**

```powerquery-m
List.Count({1, 2, 3})
```

**Output**

`3`

## Example 2

Find the number of times red appears in a list of colors, ignoring case.

**Usage**

```powerquery-m
let
    colors = {"Red", "Blue", "GREEN", "red", "Yellow", "RED"},
    redCount = List.Count(
        List.Select(colors, each Text.Lower(_) = "red")
    )
in
    redCount
```

**Output**

`3`

## Example 3

Find the number of customers in a list who purchased more than $100.

**Usage**

```powerquery-m
let
    customers = {
        [CustomerID = 101, CustomerName = "Alice", AmountPurchased = 150],
        [CustomerID = 102, CustomerName = "Bob", AmountPurchased = 75],
        [CustomerID = 103, CustomerName = "Carol", AmountPurchased = 50],
        [CustomerID = 104, CustomerName = "Dave", AmountPurchased = 90],
        [CustomerID = 105, CustomerName = "Eve", AmountPurchased = 120]
    },
    highValueCustomerCount = List.Count(
        List.Select(customers, each [AmountPurchased] > 100)
    )
in
    highValueCustomerCount
```

**Output**

`2`
