
const twoSum = (nums, target) => {
    let acc = {};
    for (let i = 0; i < nums.length; i++) {
        let k = target - nums[i];
        if (k in acc) return [acc[k], i];
        acc[nums[i]] = i;
    }
    return false;
};

const twoSumRec = (nums, target, i, acc = {}) => {
    if (i >= nums.length) return false;
    let k = target - nums[i];
    if (k in acc) return [acc[k], i];
    return twoSumRec(nums, target, i + 1, { ...acc, [nums[i]]: i })
} 