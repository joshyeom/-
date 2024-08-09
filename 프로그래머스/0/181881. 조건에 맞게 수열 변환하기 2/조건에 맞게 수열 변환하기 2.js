// arr[i] >= 50 or arr[i] % 2 == 0 => arr[i] /= 2
// arr[i] < 50 or arr[i] % 2 == 1 => arr[i] = arr[i] * 2 + 1

function solution(arr){
    let state = true
    let count = 0
    while(state){
        state = check(arr)
        count += 1
    }
    return count - 1
}

function check(arr){
    let isChanged = false
    for(let i =  0; i < arr.length ; i++){
        let value = arr[i]
        
        if(value >= 50 && value % 2 == 0){
            value /= 2
        }else if(value < 50 && value % 2 == 1){
            value = value * 2 + 1
        }
        
        if(value !== arr[i]){
            arr[i] = value
            isChanged = true
        }   
    }
    
    if(isChanged){
        return true
    }else{
        return false
    }
}
