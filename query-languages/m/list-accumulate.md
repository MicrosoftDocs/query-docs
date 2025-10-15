---
description: "Learn more about: List.Accumulate"
title: "List.Accumulate"
ms.subservice: m-source
---
# List.Accumulate

## Syntax

<pre>
List.Accumulate(
    <b>list</b> as list,
    <b>seed</b> as any,
    <b>accumulator</b> as function
) as any
</pre>

## About

Accumulates a summary value from the items in the specified list using the accumulator.

* `list`: The list to iterate.
* `seed`: An initial accumulated value.
* `accumulator`: A function that takes the current state and the current item and returns the new state.

## Example 1

Accumulates the summary value from the items in the list.

**Usage**

```powerquery-m
let
    Source = List.Accumulate(
        {1, 2, 3, 4, 5},
        0,
        (runningSum, nextNumber) => runningSum + nextNumber
    )
in
    Source
```

**Output**

`15`

## Example 2

Concatenate each word in the list with a space between, but don't include a space at the beginning.

**Usage**

```powerquery-m
let
    Source = List.Accumulate(
        {"The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."},
        null,
        (fullTextSoFar, nextPart) =>
            Text.Combine({fullTextSoFar, nextPart}, " ")
    )
in
    Source
```

**Output**
`"The quick brown fox jumps over the lazy dog."`

## Example 3

Build a list of process completion times from a start date and a list of process run times.

**Usage**

```powerquery-m
let
    #"Process Duration" = 
    {
        #duration(0,1,0,0),
        #duration(0,2,0,0),
        #duration(0,3,0,0)
    },
    #"Start Time" = #datetime(2025, 9, 8, 19, 0, 0),
    #"Process Timeline" = List.Accumulate(
        #"Process Duration",
        {#"Start Time"},
        (accumulatedTimes, nextDuration) => 
            accumulatedTimes & {List.Last(accumulatedTimes) + nextDuration}
    )
in
    #"Process Timeline"
```

**Output**

```powerquery-m
{
    #datetime(2025, 9, 8, 19, 0, 0),
    #datetime(2025, 9, 8, 20, 0, 0),
    #datetime(2025, 9, 8, 22, 0, 0),
    #datetime(2025, 9, 9, 1, 0, 0)
}
```
