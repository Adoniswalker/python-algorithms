function closestNumbers(numbers) {
    numbers.sort(function(a, b){return a - b});
    let min = Number.MAX_SAFE_INTEGER;
    for(let i=0; i <= numbers.length; i++) {
        min_a = Math.abs(numbers[i +1] - numbers[i])
        if( min_a< min && min_a !== 0){
            min = min_a;
        }
    }

    for(let i=0; i <= numbers.length; i++) {
        if(Math.abs(numbers[i +1] - numbers[i]) === min ){
            console.log(numbers[i], numbers[i+1]);
        }
    }
}

closestNumbers([4,4,-2,-1,3]) //-2 -1, 3,4
closestNumbers([5,-9, -5, 9, 10, 12]) //9, 10
// closestNumbers([])
// closestNumbers([])
