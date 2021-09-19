function count_secret_pairs(upperBound, lowerBound, consecutiveDifference) {
    // Initial Variable Setting
    var highest_sum, lowest_sum, sum = 0,0,0
    for value in consecutiveDifference{
        sum += value
        highest_sum = max(sum, highest_sum)
        lowest_sum = min(sum, lowest_sum)
    }
    // Need to +1 because of combination  = difference +1 ( count of ([2,3,4,5]) = (5-2) +1)
    result = (upperBound - lowerBound + (lowest_sum - highest_sum + 1))
    if (result < 0){
    return 0}
else{
    return result}
}
