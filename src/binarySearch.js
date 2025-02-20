const searchN = (list, n) =>
    binarySearch(list, 0, list.length - 1, n);



const binarySearch = (list, start, end, n) => {
    let m = start + Math.floor((end - start) / 2);
    if (start > end) return -1;
    return list[m] == n
        ? m
        : list[m] < n
            ? binarySearch(list, m + 1, end, n)
            : binarySearch(list, start, m - 1, n)
}


console.log(searchN([1, 2, 3, 5, 6, 9, 12, 15], 56));
