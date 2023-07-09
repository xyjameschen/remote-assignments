function max(numbers) {
    
    if (numbers.length === 0) {
      return undefined; 
    }
  
    let max_num = numbers[0]; 
  
    for (let i = 1; i < numbers.length; i++) {
      if (numbers[i] > max_num) {
        max_num = numbers[i]; 
      }
    }
    return max_num; 
  }

// console.log( max([5, 100, 33, 400, 902]) );