function find_position(numbers, target) {
    
    for (let i = 0; i < numbers.length; i++) {
      if (numbers[i] === target) {
        return i; 
      }
    }

    return -1; 
  }
 
//console.log( find_position([5, 2, 7, 7, 7, 1, 6], 7) );
