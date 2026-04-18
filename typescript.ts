const EVEN = Symbol("even");
const ODD  = Symbol("odd");

const Parity = {
    Even: EVEN,
    Odd:  ODD
} as const;

type Parity = typeof Parity[keyof typeof Parity];

function* isEvenElseIsOddGenerator() {
    let i = 0;
    let p = Parity.Even;
    while (true) {
        yield function (x: number, increment: number) {
            if (x === i) {
                return p as Parity;
            }
            p = p === Parity.Even
                ? Parity.Odd
                : Parity.Even;
            i += increment;
            return undefined;
        }
    }
}

const evaluate = (x: number) => {

    if (Number.isNaN(x) ||
        x === Infinity ||
        x === -Infinity
    ) {
        console.error(
            `I must apologize! I regret that I am unable to evaluate the \n` +
            `parity of the number ${
                x === Infinity ? "Infinity" :
                x === -Infinity ? "-Infinity" : "NaN (Not a Number)"} due to\n` +
            `arithmetic limitations.`
        );
        return;
    }

    console.log(
        `Please be patient, I am evaluating the parity of the \n` +
        `numeric input you provided: ${x}\n\nEvaluating...\n`
    );

    const startTime = performance.now();
    const increment = x < 0 ? -1 : 1;
    const generator = isEvenElseIsOddGenerator();
    const fns = Array.from(
        { length: Math.abs(x) + 1 },
        (_, _i) => generator.next().value?.bind(null, x, increment)
    );
    let result: Parity | undefined = undefined;
    let i = 0;
    while (!result) {
        result = fns[i]?.call(null);
        i++;
    }
    const endTime = performance.now();
    const t = endTime - startTime;

    console.log(
        `I have the result now. Using advanced performance\n` +
        `optimizations, I determined that your number is:\n\n` +
        `${result === Parity.Even
            ? "Even" : result === Parity.Odd
            ? "Odd" : "Unusual"}\n\n` +
        `I took ${t}ms to arrive at a confident determination.`
    );
}

/* Examples and tests */
(() => {
    evaluate(1);
    evaluate(100);
    evaluate(99999999);
    evaluate(0);
    evaluate(-0);
    evaluate(-1);
    evaluate(NaN);
    evaluate(Infinity);
    evaluate(-Infinity);
})();