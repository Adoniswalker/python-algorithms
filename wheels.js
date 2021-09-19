
function find_wheels(vehicles){
    for(let i =0; i<vehicles.length;i++) {
        if(vehicles[i]%2 !== 0) {
            vehicles[i] = 0;
            continue;
        }
        vehicles[i] = Math.trunc(vehicles[i] / 4) + 1;
    }
    return vehicles;
}

console.log(find_wheels([4,5,6, 8, 12]))

4,4,4
4, 4, 2, 2
4,2,2,2,2
2,2,2,2,2,2
