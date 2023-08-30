---
description: "Learn more about: List.Single"
title: "List.Single"
---
# List.Single

## Syntax

<pre>
List.Single(<b>list</b> as list) as any  
</pre>
  
## About

If there is only one item in the list `list`, returns that item. If there is more than one item or the list is empty, the function throws an exception.

## Example 1

Find the single value in the list {1}.

**Usage**

```powerquery-m
List.Single({1})
```

**Output**

`1`

## Example 2

Find the single value in the list {1, 2, 3}.

**Usage**

```powerquery-m
List.Single({1, 2, 3})
```

**Output**

`[Expression.Error] There were too many elements in the enumeration to complete the operation.`
