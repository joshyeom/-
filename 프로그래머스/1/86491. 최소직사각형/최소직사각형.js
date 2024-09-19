function solution(sizes) {
    let f = 0
    let s = 0
    sizes.forEach(size => {
        const sorted = size.sort((a, b) => a - b)
        f = Math.max(f, sorted[0])
        s = Math.max(s, sorted[1])
    })
    return f * s
}