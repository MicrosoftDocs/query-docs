---
description: "Learn more about: Table.ReplaceValue"
title: "Table.ReplaceValue"
ms.subservice: m-source
---
# Table.ReplaceValue

## Syntax

<pre>
Table.ReplaceValue(<b>table</b> as table, <b>oldValue</b> as any, <b>newValue</b> as any, <b>replacer</b> as function, <b>columnsToSearch</b> as list) as table
</pre>
  
## About

Replaces `oldValue` with `newValue` in the specified columns of the `table`.

## Example 1

Replace the text "goodbye" with "world" in column B, matching only the entire value.

**Usage**

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [A = 1, B = "hello"],
        [A = 2, B = "goodbye"],
        [A = 3, B = "goodbyes"]
    }),
    "goodbye",
    "world",
    Replacer.ReplaceValue,
    {"B"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "hello"],
    [A = 2, B = "world"],
    [A = 3, B = "goodbyes"]
})
```

## Example 2

Replace the text "ur" with "or" in column B, matching any part of the value.

**Usage**

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [A = 1, B = "hello"],
        [A = 2, B = "wurld"]
    }),
    "ur",
    "or",
    Replacer.ReplaceText,
    {"B"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [A = 1, B = "hello"],
    [A = 2, B = "world"]
})
```

## Example 3

Anonymize the names of US employees.

**Usage**

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [Name = "Cindy", Country = "US"],
        [Name = "Bob", Country = "CA"]
    }),
    each if [Country] = "US" then [Name] else false,
    each Text.Repeat("*", Text.Length([Name])),
    Replacer.ReplaceValue,
    {"Name"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Name = "*****", Country = "US"],
    [Name = "Bob", Country = "CA"]
})
```

## Example 4

Anonymize all columns of US employees.

**Usage**

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [Name = "Cindy", Country = "US"],
        [Name = "Bob", Country = "CA"]
    }),
    each [Country] = "US",
    "?",
    (currentValue, isUS, replacementValue) =>
        if isUS then
            Text.Repeat(replacementValue, Text.Length(currentValue))
        else
            currentValue,
    {"Name", "Country"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Name = "?????", Country = "??"],
    [Name = "Bob", Country = "CA"]
})
```

## Related content

[Replacer functions](replacer-functions.md)
