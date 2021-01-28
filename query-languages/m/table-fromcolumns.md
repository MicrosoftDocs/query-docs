---
description: "Learn more about: Table.FromColumns"
title: "Table.FromColumns | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FromColumns

## Syntax

<pre>
Table.FromColumns(<b>lists</b> as list, optional <b>columns</b> as any) as table
</pre>
  
## About  
Creates a table of type `columns` from a list `lists` containing nested lists with the column names and values. If some columns have more values then others, the missing values will be filled with the default value, 'null', if the columns are nullable.

## Example 1
Return a table from a list of customer names in a list. Each value in the customer list item becomes a row value, and each list becomes a column.

```powerquery-m
Table.FromColumns({
    {1, "Bob", "123-4567"},
    {2, "Jim", "987-6543"},
    {3, "Paul", "543-7890"}
})
```

<table> <tr> <th>Column1</th> <th>Column2</th> <th>Column3</th> </tr> <tr> <td>1</td> <td>2</td> <td>3</td> </tr> <tr> <td>Bob</td> <td>Jim</td> <td>Paul</td> </tr> <tr> <td>123-4567</td> <td>987-6543</td> <td>543-7890</td> </tr> </table>

## Example 2
Create a table from a given list of columns and a list of column names.

```powerquery-m
Table.FromColumns(
    {
        {1, "Bob", "123-4567"},
        {2, "Jim", "987-6543"},
        {3, "Paul", "543-7890"}
    },
    {"CustomerID", "Name", "Phone"}
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>2</td> <td>3</td> </tr> <tr> <td>Bob</td> <td>Jim</td> <td>Paul</td> </tr> <tr> <td>123-4567</td> <td>987-6543</td> <td>543-7890</td> </tr> </table>

## Example 3
Create a table with different number of columns per row. The missing row value is null.

```powerquery-m
Table.FromColumns(
    {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    },
    {"column1", "column2", "column3"}
)
```

<table> <tr> <th>column1</th> <th>column2</th> <th>column3</th> </tr> <tr> <td>1</td> <td>4</td> <td>6</td> </tr> <tr> <td>2</td> <td>5</td> <td>7</td> </tr> <tr> <td>3</td> <td></td> <td>8</td> </tr> <tr> <td></td> <td></td> <td>9</td> </tr> </table>
