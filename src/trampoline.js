const trampoline = (fn) => (...args) => {
    let result = fn(...args);
    while (typeof result === "function") {
        result = result();
    }
    return result;
};


const factorialRecursive = (n, acc = 1) => {
    return n === 0
        ? acc
        : () => factorialRecursive(n - 1, n * acc);
};

const factorial = trampoline(factorialRecursive);

console.log(factorial(5));
console.log(factorial(100000));  
