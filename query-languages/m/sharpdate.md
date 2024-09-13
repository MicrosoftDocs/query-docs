---
description: "Learn more about: #date"
title: "#date"
---
# #date

## Syntax

<pre>
#date(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number) as date
</pre>

## About

Creates a date value from whole numbers representing the year, month, and day. Raises an error if these conditions are not true:

* 1 ≤ year ≤ 9999
* 1 ≤ month ≤ 12
* 1 ≤ day ≤ 31

## Example 1

Create a date representing December 26, 2023.

**Usage**

```powerquery-m
#date(2023, 12, 26)
```

**Output**

`#date(2023, 12, 26)`

## Example 2

Convert a date to text using a custom format and the German culture.

**Usage**

```powerquery-m
Date.ToText(#date(2023, 12, 26), [Format="dd MMM yyyy", Culture="de-DE"])
```

**Output**

`26 Dez 2023`

## Example 3

Get the rows from a table that contain a date in 2023.

**Usage**

```powerquery-m
let
Source = #table(type table [Account Code = text, Posted Date = date, Sales = number],
    {
        {"US-2004", #date(2023,1,20), 580},
        {"CA-8843", #date(2023,7,18), 280},
        {"PA-1274", #date(2022,1,12), 90},
        {"PA-4323", #date(2023,4,14), 187},
        {"US-1200", #date(2022,12,14), 350},
        {"PTY-507", #date(2023,6,4), 110}
    }),
    #"Filtered rows" = Table.SelectRows(
        Source, 
        each Date.Year([Posted Date]) = 2023
    )
in
    #"Filtered rows"
```

**Output**

```powerquery-m
#table (type table [Account Code = text, Posted Date = date, Sales = number],
{
    {"US-2004", #date(2023, 1, 20), 580},
    {"CA-8843", #date(2023, 7, 18), 280},
    {"PA-4323", #date(2023, 4, 14), 187},
    {"PTY-507", #date(2023, 6, 4), 110}
})
```
