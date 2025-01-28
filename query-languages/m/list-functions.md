---
description: "Learn more about: List functions"
title: "List functions"
ms.date: 1/28/2025
ms.custom: "nonautomated-date"
---
# List functions

These functions create and manipulate list values.

## Information

|Name|Description|
|------------|---------------|
|[List.Count](list-count.md)|Returns the number of items in a list.|
|[List.IsEmpty](list-isempty.md)|Returns `true` if the list is empty.|
|[List.NonNullCount](list-nonnullcount.md)|Returns the number of non-null items in the list.|

## Selection

|Name|Description|
|------------|---------------|
|[List.Alternate](list-alternate.md)|Returns a list comprised of all the odd numbered offset elements in a list.|
|[List.Buffer](list-buffer.md)|Buffers a list.|
|[List.Distinct](list-distinct.md)|Returns a list of values with duplicates removed.|
|[List.FindText](list-findtext.md)|Returns a list of values (including record fields) that contain the specified text.|
|[List.First](list-first.md)|Returns the first value of the list or the specified default if empty.|
|[List.FirstN](list-firstn.md)|Returns the first set of items in the list by specifying how many items to return or a qualifying condition.|
|[List.InsertRange](list-insertrange.md)|Inserts values into a list at the given index.|
|[List.IsDistinct](list-isdistinct.md)|Indicates whether there are duplicates in the list.|
|[List.Last](list-last.md)|Returns the last value of the list or the specified default if empty.|
|[List.LastN](list-lastn.md)|Returns the last value in the list. Can optionally specify how many values to return or a qualifying condition.|
|[List.MatchesAll](list-matchesall.md)|Returns `true` if the condition function is satisfied by all values in the list.|
|[List.MatchesAny](list-matchesany.md)|Returns `true` if the condition function is satisfied by any value.|
|[List.Positions](list-positions.md)|Returns a list of offsets for the input.|
|[List.Range](list-range.md)|Returns a subset of the list beginning at an offset.|
|[List.Select](list-select.md)|Returns a list of values that match the condition.|
|[List.Single](list-single.md)|Returns the one list item for a list of length one, otherwise throws an exception.|
|[List.SingleOrDefault](list-singleordefault.md)|Returns the one list item for a list of length one and the default value for an empty list.|
|[List.Skip](list-skip.md)|Returns a list that skips the specified number of elements at the beginning of the list.|

## Transformation functions

|Name|Description|
|------------|---------------|
|[List.Accumulate](list-accumulate.md)|AAccumulates a summary value from the items in the list.|
|[List.Combine](list-combine.md)|Returns a single list by combining multiple lists.|
|[List.ConformToPageReader](list-conformtopagereader.md)|This function is intended for internal use only.|
|[List.RemoveFirstN](list-removefirstn.md)|Returns a list that skips the specified number of elements at the beginning of the list.|
|[List.RemoveItems](list-removeitems.md)|Removes items from the first list that are present in the second list.|
|[List.RemoveLastN](list-removelastn.md)|Returns a list that removes the specified number of elements from the end of the list.|
|[List.RemoveMatchingItems](list-removematchingitems.md)|Removes all occurrences of the input values.|
|[List.RemoveNulls](list-removenulls.md)|Removes all `null` values from the specified list.|
|[List.RemoveRange](list-removerange.md)|Removes count number of values starting at the specified position.|
|[List.Repeat](list-repeat.md)|Returns a list that is `count` repetitions of the original list.|
|[List.ReplaceMatchingItems](list-replacematchingitems.md)|Replaces occurrences of existing values in the list with new values that match the condition.|
|[List.ReplaceRange](list-replacerange.md)|Replaces `count` number of values starting at `position` with the replacement values.|
|[List.ReplaceValue](list-replacevalue.md)|Searches a list for the specified value and replaces it.|
|[List.Reverse](list-reverse.md)|Reverses the order of values in the list.|
|[List.Split](list-split.md)|Splits the specified list into a list of lists using the specified page size.|
|[List.Transform](list-transform.md)|Returns a new list of values computed from this list.|
|[List.TransformMany](list-transformmany.md)|Returns a list whose elements are transformed from the input list using specified functions.|
|[List.Zip](list-zip.md)|Returns a list of lists by combining items at the same position in multiple lists.|

## Membership functions

Since all values can be tested for equality, these functions can operate over heterogeneous lists.

|Name|Description|
|------------|---------------|
|[List.AllTrue](list-alltrue.md)|Returns `true` if all expressions are true.|
|[List.AnyTrue](list-anytrue.md)|Returns true if any expression is true.|
|[List.Contains](list-contains.md)|Indicates whether the list contains the value.|
|[List.ContainsAll](list-containsall.md)|Indicates where a list includes all the values in another list.|
|[List.ContainsAny](list-containsany.md)|Indicates where a list includes any of the values in another list.|
|[List.PositionOf](list-positionof.md)|Returns the offset(s) of a value in a list.|
|[List.PositionOfAny](list-positionofany.md)|Returns the first offset of a value in a list.|

## Set operations

|Name|Description|
|------------|---------------|
|[List.Difference](list-difference.md)|Returns the difference of the two given lists.|
|[List.Intersect](list-intersect.md)|Returns the intersection of the list values found in the input.|
|[List.Union](list-union.md)|Returns the union of the list values found in the input.|

## Ordering

Ordering functions perform comparisons. All values that are compared must be comparable with each other. This means they must all come from the same datatype (or include null, which always compares smallest). Otherwise, an `Expression.Error` is thrown.

Comparable data types include:

- Number
- Duration
- DateTime
- Text
- Logical
- Null

|Name|Description|
|------------|---------------|
|[List.Max](list-max.md)|Returns the maximum value or the default value for an empty list.|
|[List.MaxN](list-maxn.md)|Returns the maximum value(s) in the list. The number of values to return or a filtering condition must be specified.|
|[List.Median](list-median.md)|Returns the median value in the list.|
|[List.Min](list-min.md)|Returns the minimum value or the default value for an empty list.|
|[List.MinN](list-minn.md)|Returns the minimum value(s) in the list. The number of values to return or a filtering condition may be specified.|
|[List.Sort](list-sort.md)|Sorts a list of data according to the criteria specified.|
|[List.Percentile](list-percentile.md)|Returns one or more sample percentiles corresponding to the given probabilities.|

## Averages

These functions operate over homogeneous lists of Numbers, DateTimes, and Durations.

|Name|Description|
|------------|---------------|
|[List.Average](list-average.md)|Returns the average of the values. Works with number, date, datetime, datetimezone and duration values.|
|[List.Mode](list-mode.md)|Returns the most frequent value in the list.|
|[List.Modes](list-modes.md)|Returns a list of the most frequent values in the list.|
|[List.StandardDeviation](list-standarddeviation.md)|Returns a sample based estimate of the standard deviation. This function performs a sample based estimate. The result is a number for numbers, and a duration for DateTimes and Durations.|

## Addition

These functions work over homogeneous lists of Numbers or Durations.

|Name|Description|
|------------|---------------|
|[List.Sum](list-sum.md)|Returns the sum of the items in the list.|

## Numerics

These functions only work over numbers.

|Name|Description|
|------------|---------------|
|[List.Covariance](list-covariance.md)|Returns the covariance between the two lists of numbers.|
|[List.Product](list-product.md)|Returns the product of the numbers in the list.|

## Generators

These functions generate list of values.

|Name|Description|
|------------|---------------|
|[List.Dates](list-dates.md)|Generates a list of `date` values given an initial value, count, and incremental duration value.|
|[List.DateTimes](list-datetimes.md)|Generates a list of `datetime` values given an initial value, count, and incremental duration value.|
|[List.DateTimeZones](list-datetimezones.md)|Generates a list of `datetimezone` values given an initial value, count, and incremental duration value.|
|[List.Durations](list-durations.md)|Generates a list of `duration` values given an initial value, count, and incremental duration value.|
|[List.Generate](list-generate.md)|Generates a list of values.|
|[List.Numbers](list-numbers.md)|Returns a list of numbers given an initial value, count, and optional increment value.|
|[List.Random](list-random.md)|Returns a list of random numbers.|
|[List.Times](list-times.md)|Generates a list of `time` values given an initial value, count, and incremental duration value.|

## Parameter values

### Occurrence specification

- [Occurrence.First](occurrence-type.md) = 0;
- [Occurrence.Last](occurrence-type.md) = 1;
- [Occurrence.All](occurrence-type.md) = 2;

### Sort order

- [Order.Ascending](order-type.md) = 0;
- [Order.Descending](order-type.md) = 1;

### Equation criteria

Equation criteria for list values can be specified as either:

- A function value that is either:
  - A key selector that determines the value in the list to apply the equality criteria.
  - A comparer function that is used to specify the kind of comparison to apply. Built in comparer functions can be specified&mdash;go to [Comparer functions](comparer-functions.md).
- A list value that has:
  - Exactly two items.
  - The first element is the key selector as specified above.
  - The second element is a comparer as specified above.

For more information and examples, go to [List.Distinct](list-distinct.md).

### Comparison criteria

Comparison criterion can be provided as either of the following values:

- A number value to specify a sort order. For more information, go to [Sort order](#sort-order).
- To compute a key to be used for sorting, a function of one argument can be used.
- To both select a key and control order, comparison criterion can be a list containing the key and order.
- To completely control the comparison, a function of two arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs. [Value.Compare](value-compare.md) is a method that can be used to delegate this logic.

For more information and examples, go to [List.Sort](list-sort.md).

### Replacement operations

Replacement operations are specified by a list value. Each item of this list must be:

- A list value of exactly two items.
- First item is the old value in the list, to be replaced.
- Second item is the new value, which should replace all occurrences of the old value in the list.
