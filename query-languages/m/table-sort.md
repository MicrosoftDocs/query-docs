---
title: "Table.Sort | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Sort

## Syntax

<pre>
Table.Sort(<b>table</b> as table, <b>comparisonCriteria</b> as any) as table
</pre>
  
## About  
Sorts the `table` using the list of one or more column names and optional `comparisonCriteria` in the form { { col1, comparisonCriteria }, {col2} }.

## Example 1
Sort the table on column "OrderID".

```powerquery-m
Table.Sort(
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
        [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
        [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
        [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
        [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
        [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
        [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
    }),
    {"OrderID"}
)
```

<table> <tr> <th>OrderID</th> <th>CustomerID</th> <th>Item</th> <th>Price</th> </tr> <tr> <td>1</td> <td>1</td> <td>Fishing rod</td> <td>100</td> </tr> <tr> <td>2</td> <td>1</td> <td>1 lb. worms</td> <td>5</td> </tr> <tr> <td>3</td> <td>2</td> <td>Fishing net</td> <td>25</td> </tr> <tr> <td>4</td> <td>3</td> <td>Fish tazer</td> <td>200</td> </tr> <tr> <td>5</td> <td>3</td> <td>Bandaids</td> <td>2</td> </tr> <tr> <td>6</td> <td>1</td> <td>Tackle box</td> <td>20</td> </tr> <tr> <td>7</td> <td>5</td> <td>Bait</td> <td>3.25</td> </tr> <tr> <td>8</td> <td>5</td> <td>Fishing Rod</td> <td>100</td> </tr> <tr> <td>9</td> <td>6</td> <td>Bait</td> <td>3.25</td> </tr> </table>

## Example 2
Sort the table on column "OrderID" in descending order.

```powerquery-m
Table.Sort(
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
        [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
        [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
        [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
        [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
        [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
        [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
    }),
    {"OrderID", Order.Descending}
)
```

<table> <tr> <th>OrderID</th> <th>CustomerID</th> <th>Item</th> <th>Price</th> </tr> <tr> <td>9</td> <td>6</td> <td>Bait</td> <td>3.25</td> </tr> <tr> <td>8</td> <td>5</td> <td>Fishing Rod</td> <td>100</td> </tr> <tr> <td>7</td> <td>5</td> <td>Bait</td> <td>3.25</td> </tr> <tr> <td>6</td> <td>1</td> <td>Tackle box</td> <td>20</td> </tr> <tr> <td>5</td> <td>3</td> <td>Bandaids</td> <td>2</td> </tr> <tr> <td>4</td> <td>3</td> <td>Fish tazer</td> <td>200</td> </tr> <tr> <td>3</td> <td>2</td> <td>Fishing net</td> <td>25</td> </tr> <tr> <td>2</td> <td>1</td> <td>1 lb. worms</td> <td>5</td> </tr> <tr> <td>1</td> <td>1</td> <td>Fishing rod</td> <td>100</td> </tr> </table>

## Example 3
Sort the table on column "CustomerID" then "OrderID", with "CustomerID" being in ascending order.

```powerquery-m
Table.Sort(
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
        [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
        [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
        [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
        [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25],
        [OrderID = 8, CustomerID = 5, Item = "Fishing Rod", Price = 100.0],
        [OrderID = 9, CustomerID = 6, Item = "Bait", Price = 3.25]
    }),
    {
        {"CustomerID", Order.Ascending},
        "OrderID"
    }
)
```

<table> <tr> <th>OrderID</th> <th>CustomerID</th> <th>Item</th> <th>Price</th> </tr> <tr> <td>1</td> <td>1</td> <td>Fishing rod</td> <td>100</td> </tr> <tr> <td>2</td> <td>1</td> <td>1 lb. worms</td> <td>5</td> </tr> <tr> <td>6</td> <td>1</td> <td>Tackle box</td> <td>20</td> </tr> <tr> <td>3</td> <td>2</td> <td>Fishing net</td> <td>25</td> </tr> <tr> <td>4</td> <td>3</td> <td>Fish tazer</td> <td>200</td> </tr> <tr> <td>5</td> <td>3</td> <td>Bandaids</td> <td>2</td> </tr> <tr> <td>7</td> <td>5</td> <td>Bait</td> <td>3.25</td> </tr> <tr> <td>8</td> <td>5</td> <td>Fishing Rod</td> <td>100</td> </tr> <tr> <td>9</td> <td>6</td> <td>Bait</td> <td>3.25</td> </tr> </table>
