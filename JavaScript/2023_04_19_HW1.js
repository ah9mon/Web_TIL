let stars2 = function (n,max) {
    let a = '*'
    for (let index = 0; index < max-n ; index++) {
        a = ' ' + a
    }
    for (let index2 = 0; index2 < n; index2++) {
        a = a + '**'
    }
    return a
}

for (let i = 0; i < 5; i++) {
    console.log(stars2(i,4))
}